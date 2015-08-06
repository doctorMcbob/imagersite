# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fav_camera', models.CharField(max_length=256, blank=True)),
                ('address', models.TextField(max_length=256, blank=True)),
                ('url', models.URLField(blank=True)),
                ('photo_type', models.CharField(max_length=256, blank=True)),
                ('albums', models.ManyToManyField(related_name='albums', null=True, to='photo.Album')),
                ('photos', models.ManyToManyField(related_name='photos', null=True, to='photo.Photos')),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
