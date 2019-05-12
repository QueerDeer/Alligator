from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User


class SignUpView(TemplateView):
    template_name = "sign_up.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('pass')
            password2 = request.POST.get('re_pass')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))

        return render(request, self.template_name)


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


class ProfilePageView(TemplateView):
    template_name = "user_profile.html"
