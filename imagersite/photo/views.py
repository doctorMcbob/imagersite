from django.shortcuts import render
from .models import Album, Photos


def library_view(request):
    albums = Album.objects.filter(published='public').all()
    return render(request, 'library.html', context={'albums': albums})


def album_view(request, album_id=0):
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        return render(request, 'error.html',
                      context={'error_type': '404 Not Found'})
        render(request, 'error.html', context={'error_type': '403 Forbiddon'})
    return render(request, 'album.html', context={'album': album})


def photo_view(request, photo_id=0):
    try:
        photo = Photos.objects.get(id=photo_id)
    except Photos.DoesNotExist:
        return render(request, 'error.html',
                      context={'error_type': '404 Not Found'})
    if photo.published != 'public':
        render(request, 'error.html', context={'error_type': '403 Forbiddon'})
    return render(request, 'photo.html', context={'photo': photo})
