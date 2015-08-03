from django.conf.urls import url
from .views import album_view, photo_view, library_view, add_view

urlpatterns = [
    url(r'library/$', library_view),
    url(r'album/(?P<album_id>\d+)$', album_view),
    url(r'photos/(?P<photo_id>\d+)$', photo_view),
    url(r'(?P<model>album|photos))/add/$', add_view)
]
