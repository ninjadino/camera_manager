from django.core.management.base import LabelCommand
from django.utils import timezone
from manager.models import Alert, PushoverProfile
from django.contrib.auth.models import User


class Command(LabelCommand):
    help = 'pushover profile for user'

    def handle(self, *args, **options):
        user = User.objects.get(username=args[0])
        if not any([i for i in PushoverProfile.objects.filter(user=user)]):
            PushoverProfile(
                level=0,
                user=user,
                user_token=args[1]
            ).save()

        else:
            print 'profile already here'

