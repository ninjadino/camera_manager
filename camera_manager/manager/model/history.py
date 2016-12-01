from __future__ import unicode_literals
from django.db import models
from device import Device

class Seen(models.Model):
    host = models.ForeignKey(Device)
    first_seen = models.DateTimeField(auto_created=True, auto_now=True)
    last_seen = models.DateTimeField(null=True)
    ip = models.GenericIPAddressField()



