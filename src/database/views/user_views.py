from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from database.models import myUser
from database.models import Members
from database.models import AssociationsManager
from database.models import SystemAdmin
from database.forms import *


@login_required
def user_information(request):
    user_info = myUser.objects.get(user=request.user)
    return render(request, 'user_settings/user_settings.html', {'user_info': user_info})


@login_required
def is_god(request):
    user_info = myUser.objects.get(user=request.user)
    members = Members.objects.filter(user_id=user_info)
    god = False
    print(SystemAdmin.objects.filter(user_id=user_info))
    if (SystemAdmin.objects.filter(user_id=user_info) or AssociationsManager.objects.filter(user_id=user_info)):
        god = True

    return render(request, 'event/my_event.html', {'god': god})


@login_required
def modifyUserinfo(request):
    print("yolo")

    if request.method == 'POST':

        form = modifyUser(request.POST)
        user_to_modify = myUser.objects.get(user=request.user)
        user_to_modify.mail_secondary = form.data['secondary_email']
        user_to_modify.save()
        print("yolo")

    return render(request, 'user_settings/user_settings.html', {})

def modifyUserinfoV2(request):
    print("testest")
    if request.method == 'POST':
        form = modifyV2(request.POST)
        if form.is_valid():
            user_to_modify = myUser.objects.get(user=request.user)
            user_to_modify.mail_secondary = form.data['mail_secondary']
            user_to_modify.gender = form.data['gender']
            user_to_modify.save()
            return render(request, 'user_settings/user_settings.html', {'user_info': user_to_modify})
        else:
            return render(request,'not_found.html')
    else:
        form = modifyV2(request.POST)
        return render(request, 'user_settings/user_settings.html', {'form': form})
