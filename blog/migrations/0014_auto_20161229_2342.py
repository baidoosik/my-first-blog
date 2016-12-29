# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_가격'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='가격',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
