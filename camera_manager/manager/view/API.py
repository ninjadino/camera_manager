from ..model import Device
from django.contrib.auth.models import User
from django.shortcuts import redirect, HttpResponse,  get_object_or_404
import json

def SetUserForDevice(request,device_id, username=None):

    next_page = request.GET.get('next')

    dev = get_object_or_404(Device, id = device_id)
    if username:
        user = get_object_or_404(User, username = username)
    else:
        user = None
    dev.user = user
    dev.save()

    if next_page:
        return redirect(next_page)

    else:
        return HttpResponse('Done')




def DeviceActivity(request, device_id):
    pd = """?([\n
[Date.UTC(2014,9,7),0.7893],\n
[Date.UTC(2014,9,8),0.7853],\n
[Date.UTC(2014,9,9),0.7880],\n
[Date.UTC(2014,9,10),0.7919],\n
[Date.UTC(2014,9,12),0.7912],\n
[Date.UTC(2014,9,13),0.7842],\n
[Date.UTC(2014,9,14),0.7900],\n
[Date.UTC(2014,9,15),0.7790],\n
]);"""
    return HttpResponse(json.dumps(pd))




