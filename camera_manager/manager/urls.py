from django.conf.urls import url, include
from url.base import base_urlpatterns
from view import *

urlpatterns = [
    url(r'', include(base_urlpatterns)),
]