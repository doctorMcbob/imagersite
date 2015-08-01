import Algorithmia
import base64


input = <somefile.jpg>
request = urllib2.Request('https://api.algorithmia.com/v1/algo/ANaimi/FaceDetection/0.1.0')
request.add_header('Content-Type', 'application/json')
request.add_header('Authorization', 'API_KEY')
response = urllib2.urlopen(request, json.dumps(input))
print response.read()

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


def set_faces(request, id):
    if request.method != 'POST':
        return HttpResponse("Method must be POST")

    photo = Photo.objects.get(id=id)
    fid = request.POST.get('id', 0)
    face = Face.objects.get('id'=fid)
    face.name = request.POST.get('name', 'unknown')
    face.save()

    return HttpResponse("Done.")

# <script type="text/javescript">
#     Face.Tagger.init:
#         labelUR:: "contains"






