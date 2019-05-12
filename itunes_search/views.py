from django.views.generic import TemplateView

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
                               item['primaryGenreName'], item['country'], item['collectionViewUrl']))

        context.update({'artists': artists})
        return context
