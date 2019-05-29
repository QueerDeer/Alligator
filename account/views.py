from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver

from .forms import RegisterForm
from .models import Profile, Podcast, PodcastGenre

import requests
from pyPodcastParser.Podcast import Podcast as PyPodcast


class SignUpView(TemplateView):
    template_name = "sign_up.html"

    def dispatch(self, request, *args, **kwargs):
        form = RegisterForm()

        if request.method == 'POST':
            form = RegisterForm(request.POST)

            if form.is_valid():
                user = self.create_new_user(form)
                login(request, user)
                return redirect("/")

        context = {
            'form':     form
        }

        return render(request, self.template_name, context)

    def create_new_user(self, form):
        user = User.objects.create_user(form.cleaned_data['username'],
                                        form.cleaned_data['email'],
                                        form.cleaned_data['password'])
        Profile.objects.create(user=user)
        return user


class SignInView(TemplateView):
    template_name = "sign_in.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                context['error'] = "Login or password is incorrect"
        return render(request, self.template_name, context)


class SignOutView(View):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")


class ProfilePageView(TemplateView):
    template_name = "user_profile.html"

    def dispatch(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.get(user=request.user)
            context = {
                'subscriptions': profile.subscribes
            }
        except Profile.DoesNotExist:
            context = {}

        return render(request, self.template_name, context)


from django.http import HttpResponse
def subscribe(request):
    feed_url = request.GET.get('feed')
    id = uuid.uuid3(uuid.NAMESPACE_DNS, feed_url)

    try:
        p = Podcast.objects.get(id=id)
    except Podcast.DoesNotExist:
        podcast = PyPodcast(requests.get(feed_url).content)
        if podcast.itunes_categories:
            try:
                primary_genre = PodcastGenre.objects.get(name=podcast.itunes_categories[0])
            except PodcastGenre.DoesNotExist:
                primary_genre = None
        else:
            primary_genre = None

        p = Podcast.objects.create(id=id,
                                   author=podcast.itunes_author_name,
                                   title=podcast.title,
                                   description=podcast.description,
                                   feed_url=feed_url,
                                   primary_genre=primary_genre,
                                   image_url=podcast.itune_image)
        # p.save()

    try:
        profile = Profile.objects.get(user=request.user)
        profile.subscribes.add(p)
        profile.save()
    except Profile.DoesNotExist:
        pass

    return HttpResponse()


@receiver(post_save, sender=Podcast, dispatch_uid='update_podcast_listeners')
def update_podcast_listeners(sender, instance, **kwargs):
    """
        Update Podcast.genres, when its saved to db
    """
    title = instance.title
    feed_url = instance.feed_url
    response = requests.get('https://itunes.apple.com/search?term={}&entity=podcast'.format(title), timeout=(21, 21))

    if response.ok:
        response = response.json()
        if response['resultCount']:
            info = next(item for item in response['results'] if item['feedUrl'] == feed_url)
            genres = [int(x) for x in info['genreIds']]
            for genre in genres:
                instance.genres.add(PodcastGenre.objects.get(id=genre))
