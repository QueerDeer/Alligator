from django.core.management.base import BaseCommand, CommandError

import requests

from account.models import PodcastGenre


class Command(BaseCommand):
    help = "Updates the database table with podcast\'s genres"
    resp = None

    def parse_genres(self):
        for super_genre_key, super_genre_value in self.resp.json()['26']['subgenres'].items():
            obj, created = PodcastGenre.objects.update_or_create(id=int(super_genre_value['id']),
                                                                 defaults={
                                                                     'name': super_genre_value['name'],
                                                                     'is_active': True,
                                                                     'parent': None
                                                                 })
            if super_genre_value.get('subgenres', None):
                for genre_key, genre_value in super_genre_value['subgenres'].items():
                    print('genre: ', genre_value['id'])
                    PodcastGenre.objects.update_or_create(id=int(genre_value['id']),
                                                          defaults={
                                                              'name': genre_value['name'],
                                                              'is_active': True,
                                                              'parent': obj
                                                          })

    def handle(self, *args, **options):
        self.resp = requests.get(url="https://itunes.apple.com/WebObjects/MZStoreServices.woa/ws/genres?id=26")

        if self.resp.status_code == requests.codes.ok:
            PodcastGenre.objects.all().update(is_active=False)
            self.parse_genres()

        else:
            raise CommandError("Cannot update podcast\'s genres, because server return: {} status code"
                               .format(self.resp.status_code))

        self.stdout.write(self.style.SUCCESS('Podcast\'s genres table just successfully updated from the server'))