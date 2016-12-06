from django.core.management.base import BaseCommand, CommandError
from manager.models import Device
from manager.logger import getLogger
from django.utils import timezone

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'


    def handle(self, *args, **options):
       for dev in Device.objects.all():
           print dev.mac
           import datetime
           dev.was_seen('10.1.1.1', timezone.now() )