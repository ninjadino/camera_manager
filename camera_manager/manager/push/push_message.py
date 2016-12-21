import pushover
from django.conf import settings
pushover.init(settings.PUSHOVER_API_TOKEN)

class PushoverSender(object):
    def __init__(self, token, device_name=None):
        self.client = pushover.Client(
            user_key=token,
            device=device_name,
            api_token=settings.PUSHOVER_API_TOKEN
        )


    def send_message(self, message, title, sound=u'spacealarm'):
        self.client.send_message(message, title=title, sound=sound)



def get_sounds():
    return pushover.get_sounds()