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
def modifyUserinfo(request):
    print("yolo")

    if request.method == 'POST':

        form = modifyUser(request.POST)
        user_to_modify = myUser.objects.get(user=request.user)
        user_to_modify.mail_secondary = form.data['secondary_email']
        user_to_modify.save()
        print("yolo")


def user_modify(request):
    user_to_modify = myUser.objects.get(user=request.user)
    print(user_to_modify)
    if request.method == 'POST':
        form = modifyUser(request.POST)
        print(form.is_valid)
        if form.data['mail_secondary'] != "":
            user_to_modify.mail_secondary = form.data['mail_secondary']
        if form.data['gender'] != "":
            user_to_modify.gender = form.data['gender']
        user_to_modify.save()
        return render(request, 'user_settings/user_settings.html', {'user_info': user_to_modify})
    form = modifyUser()
    return render(request, 'user_settings/modify_user.html', locals(), {'user_info': user_to_modify})
