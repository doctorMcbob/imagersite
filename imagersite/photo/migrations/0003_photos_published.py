# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20150727_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='published',
            field=models.CharField(default='private', max_length=256, choices=[('private', 'private'), ('public', 'public')]),
        ),
    ]
