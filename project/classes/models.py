from django.db import models
from profiles.models import UserProfile


CLASSES = (
    ('Math 75', 'Math 75'),
    ('Math 84', 'Math 84'),
    ('Math 85', 'Math 85'),
    ('Math 97', 'Math 97'),
    ('Math 98', 'Math 98'),
    ('Math 99', 'Math 99'),
    ('Math 107', 'Math 107'),
    ('Math 130', 'Math 130'),
    ('Math 132', 'Math 132'),
    ('Math 138', 'Math 138'),
    ('Math 141', 'Math 141'),
    ('Math 142', 'Math 142'),
    ('Math 148', 'Math 148'),
    ('Math 151', 'Math 151'),
    ('Math 152', 'Math 152'),
    ('Math 153', 'Math 153'),
    ('Math 208', 'Math 208'),
    ('Math 238', 'Math 238'),
    ('Math 240', 'Math 240'),
    ('Math 254', 'Math 254'),
    ('Math 342', 'Math 342')
    )


class Course(models.Model):
    user = models.ForeignKey(UserProfile)
    course = models.CharField(max_length=50, choices=CLASSES)


