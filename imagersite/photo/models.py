from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Photos(models.Model):
    image = models.ImageField(upload_to='photo_files/%y-%m-%d')
    user = models.ForeignKey(User, null=False)
    title = models.CharField(max_length=256)
    description = models.TextField()
    published = models.CharField(
        max_length=256,
        choices=(('private', 'private'), ('public', 'public')),
        default='private'
    )
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Album(models.Model):
    user = models.ForeignKey(User, null=False)
    photos = models.ManyToManyField(Photos, related_name='photo_albums')
    cover = models.ForeignKey(Photos, related_name='cover_for', null=True)

    title = models.CharField(max_length=256)
    description = models.TextField()
    published = models.CharField(
        max_length=256,
        choices=(('private', 'private'), ('public', 'public')),
        default='private'
    )
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
