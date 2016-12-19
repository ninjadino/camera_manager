import pushover
from django.conf import settings
class PushoverSender(object):
    def __init__(self, token, device_name=None):
        self.client = pushover.Client(
            user_key=token,
            device=device_name,
            api_token=settings.PUSHOVER_API_TOKEN
        )



    def send_message(self, message, title, sound=u'spacealarm'):
        self.client.send_message(message, title=title, sound=sound)





if __name__ == '__main__':
    pn = PushoverSender("uef5ftb78i9w8fvp7nv2ohrjiptqxn", "iphone-de-raf")
    import time
    time.sleep(30)
    pn.send_message('FLORIAN A UN PETIT ZIZI', "nemlord")