from ..model import Device, Seen
from django.contrib.auth.models import User
from django.shortcuts import redirect, HttpResponse,  get_object_or_404
import json, datetime

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
    dev = get_object_or_404(
        Device,
        id=device_id
    )
    activity = list()
    for seen in Seen.objects.filter(host=dev):
        activity.append({'y': (seen.first_seen - datetime.timedelta(seconds=1)).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], 'a':0})
        activity.append({'y': seen.first_seen.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], 'a':1})
        activity.append({'y': seen.last_seen.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], 'a':1})
        activity.append({'y': (seen.last_seen + datetime.timedelta(seconds=1)).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], 'a':0})

    # pd = [
    #     { 'y': "2012-02-24 15:00", 'a': 20 },
    #     { 'y': "2012-02-24 16:00", 'a': 10 },
    #     { 'y': "2012-02-24 17:10", 'a': 519 },
    #     { 'y': "2012-02-24 17:10:01", 'a': 0 },
    #
    #     { 'y': "2012-02-24 18:00", 'a': 5 },
    #     { 'y': "2012-02-24 19:00", 'a': 20 }
    # ]
    return HttpResponse(json.dumps(activity))




