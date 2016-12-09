from ..model import Device
from django.contrib.auth.models import User
from django.shortcuts import redirect, HttpResponse,  get_object_or_404

def SetUserForDevice(request, username, device_id):

    next_page = request.GET.get('next')
    print
    dev = get_object_or_404(Device, id = device_id)
    user = get_object_or_404(User, username = username)

    dev.user = user
    dev.save()

    if next_page:
        return redirect(next_page)

    else:
        return HttpResponse('Done')


