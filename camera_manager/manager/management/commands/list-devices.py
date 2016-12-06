from django.core.management.base import BaseCommand, CommandError
from manager.models import Device, Seen
from django.utils import timezone
from django.conf import settings

class Command(BaseCommand):
    help = 'list active devices'


    def handle(self, *args, **options):
        min_date = timezone.now() - settings.HOST_TIMEOUT
        for dev in Seen.objects.filter(last_seen__gte = min_date):
            print "HOST:{dev.host.mac}  IP:{dev.ip}".format(**locals())


