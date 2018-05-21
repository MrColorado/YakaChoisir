from django.shortcuts import render

from database.models import Association
from database.models import myUser
from database.models import Members


def association(request):
    associations = Association.objects.all()
    return render(request, 'association/association.html/', {'associations': associations})


def my_association(request):
    my_user = myUser.objects.get(user=request.user)
    associations = Members.objects.filter(user_id=my_user)
    return render(request, 'association/my_association.html/', {'associations': associations})
