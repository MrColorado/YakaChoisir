from django import forms
from database.models import Association
from database.models import myUser

from django.forms import ModelForm
from database.models import myUser

class createEventForm(forms.Form):
    asso_list = []
    for a in Association.objects.all():
        asso_list.append((a.id, a.name))
    association_name = forms.MultipleChoiceField(required=True, widget=forms.Select(attrs={
        'class': 'form-control',
        'value': 'Association'
        }
        ), choices=asso_list)

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                                               'value': '0.0'}))
    place = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    size_intern = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                     'value': '100'}))
    size_extern = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                     'value': '100'}))
    date_begin = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control',
                                                                       'type': 'datetime-local'}))
    date_end = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control',
                                                                     'type': 'datetime-local'}))
    date_deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control',
                                                                          'type': 'datetime-local'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file',
                                                           'class': 'form-control-file'}))


class createAssociationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    date_creation = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control',
                                                                          'type': 'datetime-local'}))
    mail = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file',
                                                           'class': 'form-control'}))
    site = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    statut = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class member_list(forms.Form):
    members = []
    for m in myUser.objects.all():
        members.append((m.id, m.user.email))
    new_member = forms.MultipleChoiceField(required=True, widget=forms.Select(attrs={
   'class': 'form-control',
    'value': 'Utilisateur'
    }
    ), choices=members)
    role = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class modifyUser(forms.Form):
    secondary_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    GENDER_OPTIONS = (
        ('Male', 'M'),
        ('Female', 'F'),
    )
    gender = forms.MultipleChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
        'value': 'Gender'
    }), choices=GENDER_OPTIONS)


class modifyV2(forms.Form):
    mail_secondary = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    gender = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


