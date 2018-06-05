from django.shortcuts import render

from database.models import Association
from database.models import myUser
from database.models import Members

from database.forms import createAssociationForm
from database.forms import spec_asso
from database.forms import mod_asso


def association(request):
    associations = Association.objects.all()
    return render(request, 'association/association.html/', {'associations': associations})


def my_association(request):
    my_user = myUser.objects.get(user=request.user)
    member = Members.objects.filter(user_id=my_user)
    associations = []
    for m in member:
        associations.append(Association.objects.get(name=m.association_id))
    return render(request, 'association/my_association.html/', {'associations': associations})


def specific_association(request, asso_id):
    if request.method == 'POST':
        form = spec_asso(request.POST)
        user_id = myUser.objects.get(id=form.data['new_member'])
        role = form.data['role']
        member = Members(user_id=user_id,
                         association_id=Association.objects.get(id=asso_id),
                         role=role
                         )
        member.save()
        return render(request, 'home/index.html')
    form = spec_asso()
    res_asso = Association.objects.get(id=asso_id)
    return render(request, 'association/specific_association.html', locals(), {'res_asso': res_asso})


def modify_association(request, asso_id):
    if request.method == 'POST':
        form = mod_asso(request.POST, request.FILES)
        asso = Association.objects.get(id=asso_id)
        if form.data['description'] != "":
            asso.description = form.data['description']
        asso.photo = request.FILES['photo']
        if form.data['site'] != "":
            asso.site = form.data['site']
        if form.data['mail'] != "":
            asso.mail = form.data['mail']
        if form.data['statut'] != "":
            asso.status = form.data['statut']
        asso.save()
        return render(request, 'home/index.html')
    form = mod_asso()
    asso = Association.objects.get(id=asso_id)
    return render(request, 'association/modify_association.html', locals(), {'asso': asso})


def create_association(request):
    already = False
    if request.method == 'POST':
        form = createAssociationForm(request.POST, request.FILES)
        name = form.data['name']
        description = form.data['description']
        date_creation = form.data['date_creation']
        photo = request.FILES['photo']
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
    form = createAssociationForm()
    return render(request, 'association/create_association.html', locals())
