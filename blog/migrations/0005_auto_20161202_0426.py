# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161202_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_file_height',
            field=models.PositiveIntegerField(editable=False, default='100', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image_file_width',
            field=models.PositiveIntegerField(editable=False, default='100', null=True, blank=True),
        ),
    ]
