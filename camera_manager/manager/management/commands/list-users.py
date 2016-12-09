from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.conf import settings
import getpass
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'add user to database'

    def handle(self, *args, **options):
        for user in User.objects.all():
            print user.username, user.password

