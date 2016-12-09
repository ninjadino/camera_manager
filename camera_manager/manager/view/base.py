from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from manager.models import Device, Seen
from django.utils import timezone
from django.template import loader
from django.conf import settings
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