# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_auto_20150728_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date_published',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='photos',
            name='date_published',
            field=models.DateField(auto_now_add=True),
        ),
    ]
