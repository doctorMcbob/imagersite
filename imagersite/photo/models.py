from __future__ import unicode_literals
# from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.gis.db import models as models
# from django.contrib.gis.db import models as geomodels


@python_2_unicode_compatible
class Face(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        self.name + "'s face."


@python_2_unicode_compatible
class Photos(models.Model):
    faces = models.ManyToManyField(
        Face,
        related_name='face',
        blank=True,
    )
    image = models.ImageField(upload_to='photo_files/%y-%m-%d')
    user = models.ForeignKey(User, null=False)
    title = models.CharField(max_length=256)
    location = models.PointField(srid=900913, null=True, blank=True)
    objects = models.GeoManager()
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
    location = models.PointField(null=True, blank=True)
    objects = models.GeoManager()
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
