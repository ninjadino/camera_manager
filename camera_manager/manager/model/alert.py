from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from ..logger import getLogger
from ..push.push_message import PushoverSender
from django.utils import timezone

ALERT_LEVEL =  (
        (0, 'DEBUG'),
        (1, 'INFO'),
        (2, 'ALERT'),
        (3, 'FATAL'),
    )

class Alert(models.Model):

    message = models.CharField(max_length=512)
    title = models.CharField(max_length=200)
    date_occurrence = models.DateTimeField(auto_created=True, auto_now=True)
    level = models.IntegerField(choices=ALERT_LEVEL)

    def dispatch(self):
        profiles = list()
        for cl in ALERT_PROFILE_CLASSES:
            profiles += [profile for profile in cl.objects.filter(level__gte=self.level)]
        for profile in profiles:
            profile.send_alert(self)

HEADER_TEMPLATE ="[{curr_time}][{log_level}][{user.username}]\n"

class AlertProfile(models.Model):
    level = models.IntegerField(choices=ALERT_LEVEL)
    user = models.ForeignKey(User)
    enabled = models.BooleanField(default=True)

    def send_alert(self, alert):
        raise NotImplementedError("Almost Abstract class")


class PushoverProfile(AlertProfile):

    user_token = models.CharField(max_length=200, unique=True)
    sound = models.CharField(max_length=200, default="bugle")

    def send_alert(self, alert):
        PushoverSender(token=self.user_token).send_message(
            message=HEADER_TEMPLATE.format(user=self.user, curr_time=timezone.now(), log_level=alert.get_level_display()) + alert.message,
            title=alert.title,
            sound=self.sound
        )


class SMSAlertProfile(AlertProfile):
    number = models.CharField(max_length=50)


ALERT_PROFILE_CLASSES = [PushoverProfile, SMSAlertProfile]
