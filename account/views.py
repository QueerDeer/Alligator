from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from django.contrib.auth.models import User

from .forms import RegisterForm
from .models import Profile


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
        profile = Profile.objects.get(user=request.user)
        context = {
            'subscriptions': profile.subscribes
        }

        return render(request, self.template_name, context)
