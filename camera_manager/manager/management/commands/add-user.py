from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.conf import settings
import getpass
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'add user to database'

    def handle(self, *args, **options):
        self.stdout.write('user creation')
        username = raw_input('enter username:')
        pw = ""
        pw2 = "p"
        pw = getpass.getpass()
        pw2 = getpass.getpass('retype password:')

        while pw != pw2:
            pw = getpass.getpass('password missmatch please enter password again:')
            pw2 = getpass.getpass('retype password:')

        mail = raw_input('enter mail address:')
        new_user = User.objects.create_user(username,mail,pw)
        new_user.save()
        self.stdout.write("User {} created".format(username))



