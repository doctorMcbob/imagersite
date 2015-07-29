from django.conf.urls import url
from .views import library_view, album_view, photo_view

urlpatterns = [
    url(r'library/$', library_view),
    url(r'album/(?P<album_id>\d+)$', album_view),
    url(r'photos/(?P<photo_id>\d+)$', photo_view)
]
