from django.core.management.base import BaseCommand, CommandError
from manager.models import Device, Seen
from netmon import ARPMapNetwork, get_iface_network
from django.conf import settings
from django.core.exceptions import ValidationError

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'


    def handle(self, *args, **options):
        net = get_iface_network(settings.MONITORED_INTERFACE or 'eth0')
        for dev in ARPMapNetwork(net):

            try:
                if isinstance(dev, tuple):
                    print dev
                    Device(
                        mac = dev[1]
                    ).save()

            except ValidationError:
                pass


