"""Alligator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name="homepage"),
    re_path(r'^podcast$', PodcastView.as_view(), name="current podcast"),
    re_path(r'^podcast/detail$', PodcastDetailView.as_view(), name="current episode"),

    path('', include('api.urls')),
    path('', include('account.urls'))

]
