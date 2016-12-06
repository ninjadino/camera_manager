from django.conf.urls import url, include
from ..view.base import index, device_list

base_urlpatterns = [
    url(r'^$',index),
    url(r'^list_devices',device_list),
]
