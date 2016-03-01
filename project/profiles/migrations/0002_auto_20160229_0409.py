# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='grade',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'Running Start', b'Running Start'), (b'Freshman', b'Freshman'), (b'Sophomore', b'Sophomore'), (b'Junior', b'Junior'), (b'Senior', b'Senior')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='major',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'Finance', b'Finance'), (b'Accounting', b'Accounting'), (b'Marketing', b'Marketing'), (b'Human Resources', b'Human Resources'), (b'Economics', b'Economics')]),
        ),
    ]
