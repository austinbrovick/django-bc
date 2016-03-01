from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL



GRADES = (
    ('Running Start', 'Running Start'),
    ('Freshman', 'Freshman'),
    ('Sophomore', 'Sophomore'),
    ('Junior', 'Junior'),
    ('Senior', 'Senior')
    )

MAJORS = (
    ('Finance', 'Finance'),
    ('Accounting', 'Accounting'),
    ('Marketing', 'Marketing'),
    ('Human Resources', 'Human Resources'),
    ('Economics', 'Economics')
    )

def upload_location(instance, filename):
    print "******* in upload function *************"
    location = str(instance.user.id)
    instance.url = "%s/%s" %(location, filename)
    return "%s/%s" %(location, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user_level = models.IntegerField(default=0)

    profile_picture = models.ImageField(upload_to=upload_location, null=True, blank=True)
    grade = models.CharField(max_length=30, choices=GRADES, null=True, blank=True)
    major = models.CharField(max_length=30, choices=MAJORS, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        url = reverse("profile", kwargs={"username" : self.user.username})
        return url

