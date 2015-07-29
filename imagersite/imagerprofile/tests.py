from django.test import TestCase
from .models import ImagerProfile
import factory
from . import models


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.User
    username = 'super_cool_guy_foreva'


class UserTests(TestCase):
    def setUp(self):
        self.user = UserFactory.create()

    def test_has_profile(self):
        assert self.user.profile in ImagerProfile.objects.all()

    def test_is_active(self):
        assert self.user.is_active
