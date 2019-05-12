from django.urls import re_path
from .views import *

urlpatterns = [
    re_path('itunes_search/', ItunesSearchView.as_view(), name='itunes_search')]
