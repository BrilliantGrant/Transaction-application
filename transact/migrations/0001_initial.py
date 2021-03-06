# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 15:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(null=True, upload_to='pics/')),
                ('pic_name', models.CharField(max_length=30, null=True)),
                ('likes', models.IntegerField(default=0)),
                ('pic_caption', models.TextField(null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('comments', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
