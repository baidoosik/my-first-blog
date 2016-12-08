# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20161208_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woman',
            name='anything',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
