from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from database.models import myUser
from database.models import Members
from database.models import AssociationsManager
from database.models import SystemAdmin
from database.models import Association
from database.models import Event
from database.models import Attend
from database.views import base_views
from database.forms import *
from django.http import HttpResponse
import csv
import re


def user_information(request):
    if request.method == 'GET':
        something = base_views.search(request)
        if something:
            return something
    user_info = myUser.objects.get(user=request.user)

    god = False
    if request.user.is_authenticated:
        if len(AssociationsManager.objects.filter(user_id=myUser.objects.get(user=request.user))):
            god = True
    email_user = user_info.user.email
    email_user = re.search('[@].....', email_user)
    if email_user.group(0) == "@epita":
        isfrom = "interne"
        url_photo = 'https://photos.cri.epita.net/' + user_info.user.username
    else:
        isfrom = "externe"
        url_photo = "https://pikmail.herokuapp.com/" + user_info.user.email + "?size=200"
    return render(request, 'user_settings/user_settings.html',
                  {'user_info': user_info, 'god': god, 'url_photo': url_photo, 'isfrom' : isfrom})


def user_modify(request):
    if request.method == 'GET':
        something = base_views.search(request)
        if something:
            return something
    user_to_modify = myUser.objects.get(user=request.user)
    if request.method == 'POST':
        form = modifyUser(request.POST)
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
        if e:
            for j in e:
                participants = Attend.objects.filter(event_id=j)
                intern = 0
                extern = 0
                intern_total = j.size_intern
                extern_total = j.size_extern
                for p in participants:
                    email_user = p.user_id.user.email
                    email_user = re.search('[@].....', email_user)
                    if email_user.group(0) == "@epita":
                        intern += 1
                    else:
                        extern += 1
                events.append((j, intern, extern, intern_total, extern_total))
            asso.append((i, events))
        else:
            asso.append((i, []))
    return render(request, 'user_settings/stat.html', {'stats': asso})


def csv_download(request):

    asso = []
    for i in Association.objects.all():
        events = []
        e = Event.objects.filter(association_id=i)
        if e:
            for j in e:
                participants = Attend.objects.filter(event_id=j)
                intern = 0
                extern = 0
                intern_total = j.size_intern
                extern_total = j.size_extern
                for p in participants:
                    email_user = p.user_id.user.email
                    email_user = re.search('[@].....', email_user)
                    if email_user.group(0) == "@epita":
                        intern += 1
                    else:
                        extern += 1
                events.append((j, intern, extern, intern_total, extern_total))
            asso.append((i, events))
        else:
            asso.append((i, []))

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="stat.csv"'

    writer = csv.writer(response)
    writer.writerow(['Association', 'Evenements', 'Externe present', 'Externe place',
                         'Interne present', 'Interne place'])

    for i in asso:
       for e in i[1]:
            writer.writerow([i[0], e[0].title, e[1], e[3], e[2], e[4]])

    return response
