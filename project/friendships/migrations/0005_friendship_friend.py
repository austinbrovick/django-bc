# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 06:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20160229_0409'),
        ('friendships', '0004_auto_20160302_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='friend',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='friend', to='profiles.UserProfile'),
            preserve_default=False,
        ),
    ]