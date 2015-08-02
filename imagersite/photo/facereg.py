import Algorithmia
import base64
import requests

# input = <somefile.jpg>
# request = urllib2.Request('https://api.algorithmia.com/v1/algo/ANaimi/FaceDetection/0.1.0')
# request.add_header('Content-Type', 'application/json')
# request.add_header('Authorization', 'API_KEY')
# response = urllib2.urlopen(request, json.dumps(input))
# print response.read()

# API_KEY = 'insert later'
"""above should go to different location call"""

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


def connections(request):
    conn = Face.objects.values('name').distinct()
    names = map(lambda x: x['name'], conn)

    for n in conn:
        n['imports'] = []

    for p in Photo.objects.all():
        faces = p.faces()
        for f in faces:
            all_names = map(lambda x: x.name, faces)
            curr_name = filter(lambda x: x['name'] == f.name, conn) [0]
            curr_name['imports'] += all_names

    for n in conn:
        n['imports'] = list(set(n['imports']))
        n['imports'].remove(n('name'))

    return JasonRespone(list(conn), safe = False)




