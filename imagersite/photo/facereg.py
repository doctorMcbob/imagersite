import Algorithmia
import base64
from models import Face
from imagersite.settings import MEDIA_ROOT


def get_faces(path):
    print "getting faces"
    path = MEDIA_ROOT + "/" + path
    with open(path, 'rb') as img:
        bimage = base64.b64encode(img.read())

    Algorithmia.apiKey = 'Simple totally_real_api_key'
    result = Algorithmia.algo('/ANaimi/FaceDetection').pipe(bimage)

    faces = []
    for rect in result:
        print "found face"
        face = Face()
        face.name = "Anon"
        face.x = rect['x']
        face.y = rect['y']
        face.width = rect['width']
        face.height = rect['height']
        faces.append(face)
        Face.save(face)
    return faces
