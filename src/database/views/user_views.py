from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from database.models import myUser
from database.models import Members
from database.models import AssociationsManager
from database.models import SystemAdmin
from database.forms import *
import re


def user_information(request):
    user_info = myUser.objects.get(user=request.user)

    email_user = user_info.user.email
    email_user = re.search('[@].....', email_user)
    if email_user.group(0) == "@epita":
        isfrom = "interne"
        url_photo = 'https://photos.cri.epita.net/' + user_info.user.username
    else:
        isfrom = "externe"
        url_photo = "https://pikmail.herokuapp.com/" + user_info.user.email + "?size=200"
    return render(request, 'user_settings/user_settings.html',
                  {'user_info': user_info, 'url_photo': url_photo, 'isfrom' : isfrom})



def user_modify(request):
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
