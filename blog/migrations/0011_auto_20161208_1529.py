# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20161208_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='man',
            name='anything',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='woman',
            name='anything',
            field=models.TextField(null=True),
        ),
    ]
