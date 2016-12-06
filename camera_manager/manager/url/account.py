from django.conf.urls import url, include
from django.contrib.auth.views import  login, logout
import os

account_urlpatterns = [
    url(r'login/$',login),
    url(r'logout/$',logout, ),
]
