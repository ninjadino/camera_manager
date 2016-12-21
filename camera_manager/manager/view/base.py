from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from manager.models import Device, Seen, get_alert_profiles, ALERT_PROFILE_CLASSES
from django.utils import timezone
from django.template import loader
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
@login_required(login_url='/accounts/login/')
def index(request):
    context = {
        'title': "index"
    }
    template = loader.get_template('manager/index.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/accounts/login/')
def device_list(request):
    min_date = timezone.now() - settings.HOST_TIMEOUT
    devices = [dev for dev in Seen.objects.filter(last_seen__gte = min_date)]

    context = {
        "devices": devices,
        "users": [us for us in User.objects.all()],
        'title': "devices"
    }
    template = loader.get_template('manager/list_devices.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/accounts/login/')
def device_info(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    context = {
    'device': device
    }
    template = loader.get_template('manager/device.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/accounts/login/')
def user_info(request):
    profiles = get_alert_profiles(request.user)
    devices = Device.objects.filter(user=request.user)
    context = {
    'alert_profiles': profiles,
    'devices': devices,
    'alert_classes': ALERT_PROFILE_CLASSES
    }
    template = loader.get_template('manager/user.html')
    return HttpResponse(template.render(context, request))