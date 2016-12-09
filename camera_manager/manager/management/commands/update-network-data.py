# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from manager.models import Device, Seen
from netmon import ARPMapNetwork, get_iface_network
from netmon.core.ARP_MAP import queryNBName
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone


class Command(BaseCommand):
    help = 'scan local network and put in base'
    def handle(self, *args, **options):
        net = get_iface_network(settings.MONITORED_INTERFACE or 'eth0')
        for dev in ARPMapNetwork(net):
            try:
                if isinstance(dev, tuple):

                    try:
                        hostname = repr(queryNBName(str(dev[0])))
                        if hostname.endswith("'"):
                            hostname = hostname[:-1]
                        if hostname.startswith("'"):
                            hostname = hostname[1:]
                    except TypeError, NotImplementedError:
                        hostname = None

                    print dev, hostname
                    dev_obj = Device.objects.get_or_create(mac=dev[1])[0]
                    if hostname != dev_obj.hostname:
                        dev_obj.hostname = hostname
                        dev_obj.save()

                    dev_obj.was_seen(ip=str(dev[0]),moment=timezone.now())
            except ValidationError:
                pass




