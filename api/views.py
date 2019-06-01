from django.views.generic import TemplateView
from django.shortcuts import redirect

import requests
from urllib.parse import unquote


class Artist:
    def __init__(self, artist_name, collection_name, artwork_url, feed_url, genre, collection_url):
        self.artist_name = artist_name
        self.collection_name = collection_name
        self.artwork_url = artwork_url
        self.feed_url = feed_url
        self.genre = genre
        self.collection_url = collection_url


class PodcastInfo:
    def __init__(self, title, image_url, summary):
        self.title = title
        self.image = image_url
        self.summary = summary


class ItunesSearchView(TemplateView):
    template_name = "podcast-search.html"

    def get_context_data(self, **kwargs):
        term = self.request.GET.get('term')
        artists = []

        context = super(ItunesSearchView, self).get_context_data(**kwargs)

        response = requests.get('https://itunes.apple.com/search?term={}&entity=podcast'.format(term), timeout=(21, 21))
        if response.ok:
            response = response.json()
            if response['resultCount']:
                for item in response['results']:
                    artists.append(
                        Artist(item['artistName'], item['collectionName'], item['artworkUrl600'], item['feedUrl'],
                               item['primaryGenreName'], unquote(item['collectionViewUrl'][:-5])))

        context.update({'artists': artists})
        return context


class TopByGenreView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        genre = self.request.GET.get('genre', default=None)
        podcasts = []

        context = super(TopByGenreView, self).get_context_data(**kwargs)
        response = requests.get('https://itunes.apple.com/ru/rss/toppodcasts/genre={}/limit=100/json'.format(genre), timeout=(21, 21))

        if response.ok:
            response = response.json()
            if response.get('feed', {}).get('entry', []):
                for item in response['feed']['entry']:
                    podcasts.append(
                        PodcastInfo(item['im:name']['label'],
                                    item['im:image'][-1]['label'].replace('170x170bb-85.png', '330x330bb-85.png'),
                                    item.get('summary', {}).get('label', ''))
                    )

        context.update({'podcasts': podcasts})
        return context


def redirect_to_podcast_by_name(title: str):
    response = requests.get('https://itunes.apple.com/search?term={}&entity=podcast'.format(title), timeout=(21, 21))
    if response.ok:
        response = response.json()
        if response['resultCount']:
            return redirect('current podcast', feed=response['results'][0]['feed_url'])
