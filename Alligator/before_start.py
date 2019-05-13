from account.models import PodcastGenre


def genre_tree():
    root = PodcastGenre.objects.get(parent__isnull=True)
    res = {
        'id':       root.id,
        'name':     root.name,
        'children': []
    }

    for super_genre in PodcastGenre.objects.filter(parent=root.id):
        if PodcastGenre.objects.filter(parent=super_genre.id).exists():
            genre_list = []
            for genre in PodcastGenre.objects.filter(parent=super_genre.id):
                genre_list.append({
                    'id': genre.id,
                    'name': genre.name
                })
            res['children'].append({
                'id': super_genre.id,
                'name': super_genre.name,
                'children': genre_list
            })

        else:
            res['children'].append({
                'id': super_genre.id,
                'name': super_genre.name
            })

    return res
