from django.conf.urls import url, include
from ..view.base import index

base_urlpatterns = [
    url(r'$',index),
]
