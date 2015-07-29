# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_photos_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='published',
            field=models.CharField(default='private', max_length=256, choices=[('private', 'private'), ('public', 'public')]),
        ),
        migrations.RemoveField(
            model_name='album',
            name='photos',
        ),
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(related_name='albums', to='photo.Photos'),
        ),
    ]
