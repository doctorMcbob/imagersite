# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20150727_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='published',
            field=models.CharField(default='private', max_length=256, choices=[('private', 'private'), ('public', 'public')]),
        ),
        migrations.AddField(
            model_name='photos',
            name='published',
            field=models.CharField(default='private', max_length=256, choices=[('private', 'private'), ('public', 'public')]),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(related_name='cover_for', to='photo.Photos', null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='date_published',
            field=models.DateField(auto_now_add=True),
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
        migrations.AlterField(
            model_name='photos',
            name='date_published',
            field=models.DateField(auto_now_add=True),
        ),
    ]
