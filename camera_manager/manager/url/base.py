from django.conf.urls import url, include
from ..view.base import index, device_list, device_info, user_info

base_urlpatterns = [
    url(r'^$',index),
    url(r'^list_devices',device_list),
    url(r'^device/(?P<device_id>\d+)/$',device_info, name='device_info'),
    url(r'^user/' ,user_info, name="user_info")
]
