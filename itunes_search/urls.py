from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^/itunes_search$', views.itunes_search, name='itunes_search')]
