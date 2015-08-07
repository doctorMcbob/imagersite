from django.conf.urls import url
from .views import album_view, photo_view, library_view, add_view, edit_view, faces_view

urlpatterns = [
    url(r'^library/$', library_view, name="library_page"),
    url(r'^album/(?P<album_id>\d+)/$', album_view, name="album_page"),
    url(r'^photos/(?P<photo_id>\d+)/$', photo_view, name="photo_page"),
    url(r'^photos/(?P<photo_id>\d+)/faces', faces_view),
    url(r'^(?P<model>album|photos)/add', add_view, name="add_page"),
    url(r'^(?P<model>album|photos)/(?P<model_id>\d+)/edit', edit_view, name="edit_page")
]
