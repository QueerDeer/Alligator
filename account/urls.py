from django.urls import re_path

from .views import *


urlpatterns = [
    re_path(r'^account/login/$', SignInView.as_view(), name="sign in"),
    re_path(r'^account/register/$', SignUpView.as_view(), name="sign up"),

    re_path(r'^account/profile/$', ProfilePageView.as_view(), name="profile")
]
