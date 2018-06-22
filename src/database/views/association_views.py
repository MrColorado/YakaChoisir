from django.shortcuts import render

from database.models import Association
from database.models import AssociationsManager
from database.models import myUser
from database.models import Members

from database.forms import createAssociationForm
from database.forms import mod_asso
from database.forms import add_member_form
from database.forms import invite_member_form


def association(request):
    manager = False
    if len(AssociationsManager.objects.filter(user_id=myUser.objects.get(user=request.user))):
        manager = True
    associations = Association.objects.all()
    return render(request, 'association/association.html/', {'associations': associations, 'manager': manager})


def my_association(request):
    my_user = myUser.objects.get(user=request.user)
    member = Members.objects.filter(user_id=my_user)
    associations = []
    for m in member:
        associations.append(Association.objects.get(name=m.association_id))
    return render(request, 'association/my_association.html/', {'associations': associations})


def specific_association(request, asso_id):
    res_asso = Association.objects.get(id=asso_id)
    return render(request, 'association/specific_association.html', {'res_asso': res_asso})


def add_members(request, asso_id):
    res_asso = Association.objects.get(id=asso_id)
    current_member = []
    for c in Members.objects.all():
        if c.association_id == res_asso:
            current_member.append(c.user_id.user.first_name + " " + c.user_id.user.last_name + " " + c.role)
    if request.method == 'POST':
        form = add_member_form(request.POST)
        user_id = myUser.objects.get(id=form.data['new_member'])
        role = form.data['role']
        if role == "Retirer":
            Members.objects.filter(association_id=res_asso, user_id=user_id).delete()
            return render(request, 'association/specific_association.html', locals(),
                          {'current_member': current_member, 'res_asso': res_asso})
        member = Members(user_id=user_id,
                         association_id=Association.objects.get(id=asso_id),
                         role=role
                         )
        if len(Members.objects.filter(association_id=res_asso, user_id=user_id)):
            member = Members.objects.get(association_id=res_asso, user_id=user_id)
            member.role = role
        member.save()
        return render(request, 'association/specific_association.html', locals(),
                      {'current_member': current_member, 'res_asso': res_asso})
    form = add_member_form()
    return render(request, 'association/add_member.html', locals(),
                  {'current_member': current_member, 'res_asso': res_asso})


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
        return render(request, 'association/specific_association.html', {'res_asso': asso})
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
        president = Members(user_id=myUser.objects.get(id=form.data["president"]), association_id=assoc,
                            role="Président")
        president.save()
        vicepresident = Members(user_id=myUser.objects.get(id=form.data["vicepresident"]), association_id=assoc,
                                role="Vice-Président")
        vicepresident.save()
        tresorier = Members(user_id=myUser.objects.get(id=form.data["secretaire"]), association_id=assoc,
                            role="Trésorier")
        tresorier.save()
        secretaire = Members(user_id=myUser.objects.get(id=form.data["tresorier"]), association_id=assoc,
                             role="Secrétaire")
        secretaire.save()
        return render(request, 'home/index.html')
    form = createAssociationForm()
    return render(request, 'association/create_association.html', locals())


def invite_member(request):
    if request.method == "POST":
        form = invite_member_form(request.POST)
        print("send mail to : " + form.data["mail"])
        return render(request, "association/invite_member.html", {"form": form})
    form = invite_member_form()
    return render(request, 'association/invite_member.html', {"form": form})
