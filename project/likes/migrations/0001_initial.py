# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0003_auto_20160301_2338'),
        ('profiles', '0002_auto_20160229_0409'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts.Comment')),
                ('liker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('liker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserProfile')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
        ),
    ]