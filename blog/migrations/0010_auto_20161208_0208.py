# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_datestyle1_datestyle2_man_woman'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manstyle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Womanstyle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='man',
            name='mystyle',
            field=models.ForeignKey(default='', to='blog.Manstyle'),
        ),
        migrations.AddField(
            model_name='man',
            name='womanstyle',
            field=models.ForeignKey(to='blog.Womanstyle', null=True),
        ),
        migrations.AddField(
            model_name='woman',
            name='manstyle',
            field=models.ForeignKey(to='blog.Manstyle', null=True),
        ),
        migrations.AddField(
            model_name='woman',
            name='mystyle',
            field=models.ForeignKey(default='', to='blog.Womanstyle'),
        ),
    ]
