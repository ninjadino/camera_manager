from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
    mac = models.CharField(max_length= 200)
    hostname = models.CharField(max_length=200, null=True )
    user = models.ForeignKey(User, null=True)





