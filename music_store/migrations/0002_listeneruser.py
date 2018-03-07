# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-07 03:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListenerUser',
            fields=[
                ('defaultuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='music_store.DefaultUser')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            bases=('music_store.defaultuser',),
        ),
    ]
