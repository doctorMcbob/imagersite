from django.test import TestCase
from .models import Photos, Album
import factory
from . import models


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.User
        django_get_or_create = ('username',)
    username = 'Photo_Maker_mcCoolGuy'


class PhotoFactory(factory.DjangoModelFactory):
    class Meta:
        model = Photos
    user = UserFactory()


class AlbumFactory(factory.DjangoModelFactory):
    class Meta:
        model = Album
    user = UserFactory()


class TestPhoto(TestCase):
    def setUp(self):
        self.photo = PhotoFactory.create()

    def test_photo_has_a_user(self):
        assert self.photo.user is not None

    def test_new_photo_discription(self):
        assert self.photo.description == ''


class TestAlbum(TestCase):
    def setUp(self):
        self.photo = PhotoFactory.create()
        self.album = AlbumFactory.create()

    def test_album_user(self):
        assert self.album.user is not None
        assert self.album.user is self.photo.user
