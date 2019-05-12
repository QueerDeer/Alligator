from django.urls import path

from .views import SignInView, SignUpView


urlpatterns = [
    path('login', SignInView.as_view(), name="sign in"),
    path('register', SignUpView.as_view(), name="sign up"),
]
