from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
from photo.models import Photos, Album


class ActiveProfileManager(models.Manager):
    def get_queryset(self):
        return super(ActiveProfileManager, self).get_queryset()\
            .filter(user__is_active=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name="profile",
        null=False,
    )
    photos = models.ManyToManyField(
        Photos,
        related_name='user_photos',
        null=True,
    )
    albums = models.ManyToManyField(
        Album,
        related_name='user_albums',
        null=True,
    )
    fav_camera = models.CharField(
        max_length=256,
        blank=True
    )
    address = models.TextField(
        max_length=256,
        blank=True
    )
    url = models.URLField(
        blank=True
    )
    photo_type = models.CharField(
        max_length=256,
        blank=True
    )

    objects = models.Manager()
    active = ActiveProfileManager()

    @property
    def is_active(self):
        return self.user.is_active

    def __str__(self):
        return self.user.get_full_name() or self.user.username
