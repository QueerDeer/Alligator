from django.views.generic import TemplateView
from pyPodcastParser.Podcast import Podcast

import requests


class Artist:
    def __init__(self, artist_name, collection_name, artwork_url, feed_url, genre, country, collection_url):
        self.artist_name = artist_name
        self.collection_name = collection_name
        self.artwork_url = artwork_url
        self.feed_url = feed_url
        self.genre = genre
        self.country = country
        self.collection_url = collection_url


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        term = 'disgustingmen'
        artists = []

        context = super(HomeView, self).get_context_data(**kwargs)

        response = requests.get('https://itunes.apple.com/search?term={}&entity=podcast'.format(term), timeout=(21, 21))
        if response.ok:
            response = response.json()
            if response['resultCount']:
                for item in response['results']:
                    artists.append(
                        Artist(item['artistName'], item['collectionName'], item['artworkUrl600'], item['feedUrl'],
                               item['primaryGenreName'], item['country'], item['collectionViewUrl']))

        context.update({'artists': artists})
        return context


class PodcastView(TemplateView):
    template_name = "podcast.html"

    def get_context_data(self, **kwargs):
        feed_url = self.request.GET.get('feed')

        context = super(PodcastView, self).get_context_data(**kwargs)

        if feed_url:
            response = requests.get(feed_url)
            podcast = Podcast(response.content)
            if podcast.is_valid_rss:
                context.update({'podcast': podcast})

        return context




class PodcastDetailView(TemplateView):
    template_name = "podcast-detail.html"