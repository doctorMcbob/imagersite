from django.shortcuts import render, redirect
from .models import Album, Photos
from .forms import PhotoForm, AlbumForm


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


def add_view(request, model="photos"):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')

    if model == 'photos':
        form = PhotoForm(request.user, request.POST)
    elif model == 'album':
        form = AlbumForm(request.user, request.POST)
    else:
        raise ValueError("Expected 'photos' or 'album'. got " + model)

    if request.method == "POST":
        if form.is_valid():
            photo = form.save()
            return render(request, 'photo.html', context={'photo': photo})

    elif request.method == "GET":
        return render(request, 'add.html', context={'form': form, 'model': model})
