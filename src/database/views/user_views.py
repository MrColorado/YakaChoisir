from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import re

from database.models import myUser
from database.models import Members
from database.models import AssociationsManager
from database.models import SystemAdmin
from database.models import Association
from database.models import Event
from database.models import Attend
from database.forms import *


def user_information(request):
    user_info = myUser.objects.get(user=request.user)
    return render(request, 'user_settings/user_settings.html', {'user_info': user_info})


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


def stat(request):
    asso = []
    for i in Association.objects.all():
        events = []
        e = Event.objects.filter(association_id=i)
        for j in e:
            participants = Attend.objects.filter(event_id=j)
            intern = 0
            extern = 0
            for p in participants:
                email_user = p.user_id.user.email
                email_user = re.search('[@].....', email_user)
                if email_user.group(0) == "@epita":
                    intern += 1
                else:
                    extern += 1
            events.append((j, intern, extern))
        asso.append((i, events))
    return render(request, 'user_settings/stat.html', {'stats': asso})
