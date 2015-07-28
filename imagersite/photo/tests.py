from django.test import TestCase
import factory
from django.contrib.auth.models import User

# Create your tests here.

class UserFactory(factory.DjangoModelFactory):
    class Meta:
        