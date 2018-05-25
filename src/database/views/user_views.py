from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from database.models import myUser
from database.models import Members
from database.models import AssociationsManager
from database.models import SystemAdmin
from database.forms import modifyUser


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


def modifUser(request):
    if request.method == 'POST':
        form = modifyUser(request.POST)
        user_to_modifiy = myUser.objects.get(user=request.user)
        user_to_modifiy.mail_secondary = form.data['secondary_email']
        user_to_modifiy.save()
    else:
        form = modifyUser()
    assos = Association.objects.all()
    return render(request, 'user_settings/user_settings.html', locals(), {'assos': assos})
