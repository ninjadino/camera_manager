from django.conf.urls import url, include
from django.contrib.auth.views import  login, logout
import os
print os.path.exists('login.html')

account_urlpatterns = [
    url(r'login/$',login),
    url(r'logout/$',logout, ),
]
