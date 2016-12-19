from django.core.management.base import BaseCommand
from manager.models import Alert

template = """Alert template
should be seen on every device with
debug enabled
"""
class Command(BaseCommand):
    help = 'send a debug push message alert'

    def handle(self, *args, **options):
        Alert(
            level = 0,
            message=template,
            title='test alert',

        ).dispatch()



