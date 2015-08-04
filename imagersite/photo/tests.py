from django.test import TestCase
from django.contrib.auth import models
from .models import Photos, Album
import factory


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.User
        django_get_or_create = ('username',)
    username = 'Photo_Maker_mcCoolGuy'


class PhotoFactory(factory.DjangoModelFactory):
    class Meta:
        model = Photos
    user = factory.SubFactory(UserFactory)


class AlbumFactory(factory.DjangoModelFactory):
    class Meta:
        model = Album
    user = factory.SubFactory(UserFactory)


class TestPhoto(TestCase):
    def setUp(self):
        self.photo = PhotoFactory.create()

    def test_photo_has_a_user(self):
        assert self.photo.user is not None

    def test_new_photo_discription(self):
        assert self.photo.description == ''

    def test_photo_access(self):
        assert self.photo.published == "private"


class TestAlbum(TestCase):
    def setUp(self):
        self.user = UserFactory.create()
        self.photo = PhotoFactory.create(user=self.user)
        self.album = AlbumFactory.create(user=self.user)

    def tearDown(self):
        self.user.delete()
        self.photo.delete()
        self.album.delete()

    def test_album_user(self):
        assert self.album.user is not None

    def test_album_access(self):
        assert self.album.published == "private"
