from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^api/search$', ItunesSearchView.as_view(), name='itunes search')]
