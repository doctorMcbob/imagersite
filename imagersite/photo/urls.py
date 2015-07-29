from django.conf.url import url
from .views import library_view, album_view, photo_view

urlpatterns = [
    url(r'library/', library_view),
    url(r'album/<album_id>\d+', album_view),
    url(r'photos/<photo_id>\d+', photo_view)
]
