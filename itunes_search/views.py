from django.shortcuts import render

from django.http import HttpRequest
from django.views.decorators.http import require_GET

import requests


@require_GET
def itunes_search(request: HttpRequest):
    term = request.GET.get('term').lower()
    entity = request.GET.get('entity').lower()

    response = requests.get('https://itunes.apple.com/search?term={}&entity={}'.format(term, entity), timeout=(21, 21))
    if response.ok:
        response = response.json()
        if response['resultCount']:
            for item in response['results']:
                pass
