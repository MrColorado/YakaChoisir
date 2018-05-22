from django.shortcuts import render

from database.models import Association
from database.models import myUser
from database.models import Members

from database.forms import createAssociationForm


def association(request):
    associations = Association.objects.all()
    return render(request, 'association/association.html/', {'associations': associations})


def my_association(request):
    my_user = myUser.objects.get(user=request.user)
    associations = Members.objects.filter(user_id=my_user)
    return render(request, 'association/my_association.html/', {'associations': associations})


def create_association(request):
    already = False;
    if request.method == 'POST':
        form = createAssociationForm(request.POST)
        name = form.data['name']
        description = form.data['description']
        date_creation = form.data['date_creation']
        photo = form.data['photo']
        site = form.data['site']
        statut = form.data['statut']  # status juridique
        assoc = Association(name=name,
                            date_creation=date_creation,
                            description=description,
                            photo=photo,
                            site=site,
                            statut=statut)
        if len(Association.objects.filter(name=name)):
            already = True
            return render(request, 'association/create_association.html', locals())
        assoc.save()
    else:
        form = createAssociationForm()
    assos = Association.objects.all()
    return render(request, 'home/index.html')