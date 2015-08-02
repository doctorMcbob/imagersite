from django.views.generic import TemplateView
from photo.models import Photos
import Algorithmia
import base64
import requests


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        try:
            context["photo"] = Photos.objects.filter(published='public')\
                .order_by('?').first()
            # returns pic of dog if above is context is false/att error
        except AttributeError:
            context["photo"] = 'imagersite/media/photo_files/15-07-28/dog.jpg'
        return context


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