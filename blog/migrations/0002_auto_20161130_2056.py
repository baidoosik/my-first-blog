# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_file',
            field=models.ImageField(upload_to='static_files/uploaded/original/%Y/%m/%d'),
        ),
    ]
