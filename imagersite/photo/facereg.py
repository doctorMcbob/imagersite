import Algorithmia
import base64
from models import Face


def get_faces(path):
    with open(path, 'rb') as img:
        bimage = base64.b64encode(img.read())

    Algorithmia.apiKey = 'Simple totally_real_api_key'
    result = Algorithmia.algo('/ANaimi/FaceDetection').pipe(bimage)

    faces = []
    for rect in result:
        face = Face()
        face.name = "Anon"
        face.x = rect['x']
        face.y = rect['y']
        face.width = rect['width']
        face.height = rect['height']
        faces.append(face)
    for face in faces:
        face.save()
    return faces


def set_faces(request, photo_id):
    face_id = request.POST.get('photo_id', '0')
    face = Face.objects.get(id=face_id)
    face.name = Face.objects.get('name', 'Unknown')
    face.save()
    return face
