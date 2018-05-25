from django.shortcuts import render

from database.models import Association
from database.models import myUser
from database.models import Members

from database.forms import createAssociationForm
from database.forms import member_list


def association(request):
    associations = Association.objects.all()
    return render(request, 'association/association.html/', {'associations': associations})


def my_association(request):
    my_user = myUser.objects.get(user=request.user)
    associations = Members.objects.filter(user_id=my_user)
    return render(request, 'association/my_association.html/', {'associations': associations})


def specific_association(request, asso_id):
    if request.method == 'POST':
        form = member_list(request.POST)
        user_id = myUser.objects.get(id=form.data['new_member'])
        role = form.data['role']
        member = Members(user_id=user_id,
                         association_id=Association.objects.get(id=asso_id),
                         role=role
                         )
        member.save()
        return render(request, 'home/index.html')
    else:
        form = member_list()
        res_asso = Association.objects.filter(id=asso_id)
        if len(res_asso):
            return render(request, 'association/specific_association.html', locals(), {'res_asso': res_asso})
    return render(request, 'not_found.html')


def create_association(request):
    already = False
    if request.method == 'POST':
        form = createAssociationForm(request.POST)
        name = form.data['name']
        description = form.data['description']
        date_creation = form.data['date_creation']
        photo = form.data['photo']
        site = form.data['site']
        mail = form.data['mail']
        statut = form.data['statut']  # status juridique
        assoc = Association(name=name,
                            date_creation=date_creation,
                            description=description,
                            photo=photo,
                            site=site,
                            mail=mail,
                            statut=statut)
        if len(Association.objects.filter(name=name)):
            already = True
            return render(request, 'association/create_association.html', locals())
        assoc.save()
        return render(request, 'home/index.html')
    else:
        form = createAssociationForm()
    assos = Association.objects.all()
    return render(request, 'association/create_association.html', locals())
