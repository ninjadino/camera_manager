from __future__ import unicode_literals
from django.db import models
from device import Device

class Camera(models.Model):
    name = models.CharField(max_length=200)
    stream_port = models.IntegerField(default=8081)
    conf_port = models.IntegerField(default=80)
    host = models.ForeignKey(Device)