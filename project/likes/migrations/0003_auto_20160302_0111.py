# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 01:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0002_auto_20160301_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentlike',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='commentlike',
            name='liker',
        ),
        migrations.RemoveField(
            model_name='postlike',
            name='liker',
        ),
        migrations.RemoveField(
            model_name='postlike',
            name='post',
        ),
        migrations.DeleteModel(
            name='CommentLike',
        ),
        migrations.DeleteModel(
            name='PostLike',
        ),
    ]