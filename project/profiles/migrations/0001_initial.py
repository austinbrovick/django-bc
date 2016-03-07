# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 01:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_level', models.IntegerField(default=0)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=profiles.models.upload_location)),
                ('grade', models.CharField(blank=True, choices=[(b'Running Start', b'Running Start'), (b'Freshman', b'Freshman'), (b'Sophomore', b'Sophomore'), (b'Junior', b'Junior'), (b'Senior', b'Senior')], max_length=30, null=True)),
                ('major', models.CharField(blank=True, choices=[(b'Finance', b'Finance'), (b'Accounting', b'Accounting'), (b'Marketing', b'Marketing'), (b'Human Resources', b'Human Resources'), (b'Economics', b'Economics')], max_length=30, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
