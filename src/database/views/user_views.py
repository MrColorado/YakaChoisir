from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from database.models import myUser
from database.models import Members
from database.models import SystemAdmin

@login_required
def user_information(request):
    user_info = myUser.objects.get(user=request.user)
    return render(request, 'user_settings/user_settings.html', {'user_info': user_info})


@login_required
def is_god(request):
    user_info = myUser.objects.get(user=request.user)
    #members = Members.objects.filter(user_id=user_info)
    god = False
    if (SystemAdmin.objects.filter(user_id=user_info)):
        god = True

    return render(request, 'event/my_event.html', {'god': god})
