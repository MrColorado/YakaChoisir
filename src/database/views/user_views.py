from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
    res = []
    for i in Association.object.all():
        asso = []
        events = []
        e = Event.object.filter(association_id=i)
        for j in e:
            participants = Attend.object.filter(event_id=j)
            events.append((j, len(participants)))
        asso.append((i, events))
    return render(request, 'user_settings/statistique.html', {'stats': res})
