import Algorithmia
import base64


API_KEY = 'insert later'


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
