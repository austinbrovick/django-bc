# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20160229_0409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.CharField(max_length=50, choices=[(b'Math 75', b'Math 75'), (b'Math 84', b'Math 84'), (b'Math 85', b'Math 85'), (b'Math 97', b'Math 97'), (b'Math 98', b'Math 98'), (b'Math 99', b'Math 99'), (b'Math 107', b'Math 107'), (b'Math 130', b'Math 130'), (b'Math 132', b'Math 132'), (b'Math 138', b'Math 138'), (b'Math 141', b'Math 141'), (b'Math 142', b'Math 142'), (b'Math 148', b'Math 148'), (b'Math 151', b'Math 151'), (b'Math 152', b'Math 152'), (b'Math 153', b'Math 153'), (b'Math 208', b'Math 208'), (b'Math 238', b'Math 238'), (b'Math 240', b'Math 240'), (b'Math 254', b'Math 254'), (b'Math 342', b'Math 342')])),
                ('user', models.ForeignKey(to='profiles.UserProfile')),
            ],
        ),
    ]
