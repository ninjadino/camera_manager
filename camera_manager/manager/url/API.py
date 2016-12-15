from django.conf.urls import url, include
from ..view.API import SetUserForDevice, DeviceActivity
api_urlpatterns = [
    url(r'^change_user/(?P<device_id>\d+)/(?P<username>[\w\-]+)/$', SetUserForDevice, name="change_user"),
    url(r'^change_user/(?P<device_id>\d+)/$', SetUserForDevice, name="change_user_to_none"),
    url(r'^device/(?P<device_id>\d+)/$', DeviceActivity, name="api_device_id"),
]
