# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='portada',
            field=models.ImageField(null=True, upload_to=b'portadas'),
        ),
    ]
