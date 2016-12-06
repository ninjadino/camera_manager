from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.core.validators import validate_ipv46_address
from django.conf import settings
from manager.logger import getLogger
from manager.exceptions import NewConnection

logger = getLogger("device")

class Device(models.Model):
    mac = models.CharField(max_length= 200, unique=True)
    hostname = models.CharField(max_length=200, null=True )
    user = models.ForeignKey(User, null=True)

    def was_seen(self, ip, moment):
        '''
        The get or create Seen method but a bit more evolved. If the IP has changed a new Seen object if the last seen is
        more than SETTING.host_timeout seconds.
        :param ip:
        :param moment: datetime object
        :return: the Seen object
        :raises: ArgumentError
        '''
        _seen = None
        validate_ipv46_address(ip)
        if not isinstance(moment, datetime):
            print moment.__class__
            raise ValueError("argument error")
        try:
            last = Seen.objects.filter(host=self).latest()
            if ip != str(last.ip):
                logger.debug("ip changed: {self.mac} with ip: {ip}".format(**locals()))
                raise NewConnection
            delta = moment - last.last_seen
            if delta > settings.HOST_TIMEOUT:
                logger.debug("connection detected: {self.mac} with ip: {ip}".format(**locals()))
                raise NewConnection
            _seen = last
            last.keepalive(moment)
        except ObjectDoesNotExist:
            logger.debug("first seen: {self.mac} with ip: {ip}".format(**locals()))
            _seen = self._add_seen_entry(ip, moment)
        except NewConnection:
            _seen = self._add_seen_entry(ip, moment)
        return _seen

    def _add_seen_entry(self, ip, moment):
        _ret = Seen(host=self, last_seen=moment, ip=ip)
        _ret.save()
        return _ret





class Seen(models.Model):

    class Meta:
        get_latest_by = "last_seen"

    host = models.ForeignKey(Device)
    first_seen = models.DateTimeField(auto_created=True, auto_now=True)
    last_seen = models.DateTimeField(null=True)
    ip = models.GenericIPAddressField()

    def keepalive(self, moment):
        self.last_seen = moment
        self.save()



