from django.shortcuts import render, redirect
from .models import Album, Photos
from .forms import PhotoForm, AlbumForm


def get_faces(path):
    with open(path, 'rb') as img:
        bimage = base64.b64encode(img.read())

    Algorithmia.apiKey = 'API_KEY'
    result = Algorithmia.algo('/algo/ANaimi/FaceDetection/0.1.0').pipe(biamge)

    faces = []
    for rect in result:
        face = Face()
        face.name = person_name()
        face.x = rect['x']
        face.y = rect['y']
        face.width = rect['width']
        face.height = rect['height']
        faces.append(face)
    return faces


def set_faces(request, id):
    if request.method != 'POST':
        return HttpResponse("Method must be POST")

    photo = Photo.objects.get(id=id)
    fid = request.POST.get('id', '0')
    face = Face.objects.get(id=fid)
    face.name = request.POST.get('name', 'Unknown')
    face.save()

    return HttpResponse("Done.")


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
            the_model = form.save()
            if model == "photos":
                return render(request, 'photo.html', context={
                    'photo': the_model
                })
            elif model == "album":
                return render(request, 'album.html', context={
                    'album': the_model
                })

    elif request.method == "GET":
        return render(request, 'add.html', context={
            'form': form,
            'model': model
        })


def edit_view(request, model="photos", model_id=0):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')

    if model == "photos":
        the_model = Photos.objects.get(pk=model_id)
        form = PhotoForm(request.user, request.POST, instance=the_model)
    elif model == "album":
        the_model = Album.objects.get(pk=model_id)
        form = AlbumForm(request.user, request.POST, instance=the_model)
    else:
        raise ValueError("Expected 'photos' or 'album'/ got " + model)

    if request.user is not the_model.user:
        return render(request, 'error.html', context={
            "error_type": "403 forbidden"
        })

    if request.method == "POST":
        if form.is_valid():
            the_model = form.save()
            if model == "photos":
                return render(request, 'photo.html', context={
                    'photo': the_model
                })
            elif model == "album":
                return render(request, 'album.html', context={
                    'album': the_model
                })

    return render(request, 'edit.html', context={
        'form': form,
        'item': the_model
    })
