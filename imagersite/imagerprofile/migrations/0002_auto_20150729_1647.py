# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0006_auto_20150728_2110'),
        ('imagerprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagerprofile',
            name='albums',
            field=models.ManyToManyField(related_name='albums', null=True, to='photo.Album'),
        ),
        migrations.AddField(
            model_name='imagerprofile',
            name='photos',
            field=models.ManyToManyField(related_name='photos', null=True, to='photo.Photos'),
        ),
    ]
