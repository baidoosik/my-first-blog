# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20161207_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datestyle1',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Datestyle2',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Man',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('number', models.CharField(max_length=20)),
                ('tendency', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('major', models.CharField(max_length=30)),
                ('datestyle1', models.ForeignKey(to='blog.Datestyle1')),
                ('datestyle2', models.ForeignKey(to='blog.Datestyle2')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Woman',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('number', models.CharField(max_length=20)),
                ('tendency', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('major', models.CharField(max_length=30)),
                ('datestyle1', models.ForeignKey(to='blog.Datestyle1')),
                ('datestyle2', models.ForeignKey(to='blog.Datestyle2')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
