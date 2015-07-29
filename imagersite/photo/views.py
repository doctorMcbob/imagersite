from django.shortcuts import render
from .models import Albums, Photos


def library_view(request):
    albums = Albums.objects.filter(published='public').all()
    return render(request, 'library.html', context={'albums': albums})


def album_view(request, album_id=0):
    album = Albums.objects.get(id=album_id)
    if album.published != 'public':
        render(request, 'error.html', context={'error_type': '403 Forbiddon'})
    return render(request, 'album.html', context={'album': album})


def photo_view(request, photo_id=0):
    photo = Photos.objects.get(id=photo_id)
    if photo.published != 'public':
        render(request, 'error.html', context={'error_type': '403 Forbiddon'})
    return render(request, 'photo.html', context={'photo': photo})
