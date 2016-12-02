# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161202_0426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_file_height',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_file_width',
        ),
        migrations.AddField(
            model_name='post',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image_file', '430x360', verbose_name='cropping', hide_image_field=False, size_warning=False, free_crop=False, allow_fullsize=False, adapt_rotation=False, help_text=None),
        ),
    ]
