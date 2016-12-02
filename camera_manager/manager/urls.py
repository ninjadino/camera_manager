from django.conf.urls import url, include
from url.base import base_urlpatterns
from url.account import account_urlpatterns
from view import *

urlpatterns = [
    url(r'', include(base_urlpatterns)),
    url(r'^accounts/', include(account_urlpatterns)),

]