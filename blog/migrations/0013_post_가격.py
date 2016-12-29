# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20161208_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='가격',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
