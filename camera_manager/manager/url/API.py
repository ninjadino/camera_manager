from django.conf.urls import url, include
from ..view.API import SetUserForDevice
api_urlpatterns = [
    url(r'^change_user/(?P<device_id>\d+)/(?P<username>[\w\-]+)/$', SetUserForDevice, name="change_user"),
]
