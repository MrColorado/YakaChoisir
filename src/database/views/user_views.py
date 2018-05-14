from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from database.models import myUser


@login_required
def user_information(request):
    if request.user.is_anonymous:
        return render(request, 'not_found.html')
    user_info = myUser.objects.get(user=request.user)
    return render(request, 'user_settings/user_settings.html', {'user_info': user_info})
