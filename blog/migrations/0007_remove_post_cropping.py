# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20161202_0432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cropping',
        ),
    ]
