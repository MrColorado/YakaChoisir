from django import forms
from database.models import Association
from database.models import myUser


class createEventForm(forms.Form):
    # if forms.is_valid() :
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
    boutique = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))


class modifyEventForm(forms.Form):
    def __init__(self, *args, **kwargs):
        event = kwargs.pop('event')
        super(modifyEventForm, self).__init__(*args, **kwargs)
        self.fields['association_name'].widget = forms.TextInput(attrs={'class': 'form-control',
                                                                        'value': event.association_id})
        self.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control',
                                                             'value': event.title})
        self.fields['description'].widget = forms.Textarea(attrs={'class': 'form-control',
                                                                  'placeholder': event.description})
        self.fields['price'].widget = forms.NumberInput(attrs={'class': 'form-control',
                                                               'value': event.price})
        self.fields['place'].widget = forms.TextInput(attrs={'class': 'form-control',
                                                             'value': event.place})
        self.fields['size_intern'].widget = forms.NumberInput(attrs={'class': 'form-control',
                                                                     'value': event.size_intern})
        self.fields['size_extern'].widget = forms.NumberInput(attrs={'class': 'form-control',
                                                                     'value': event.size_extern})
        self.fields['date_begin'].widget = forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local',
                                                                      'default': event.date_begin})
        self.fields['boutique'].widget = forms.EmailField(attrs={'class': 'form-control', 'value': event.boutique})


    association_name = forms.CharField()
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
    place = forms.CharField()
    size_intern = forms.IntegerField()
    size_extern = forms.IntegerField()
    date_begin = forms.DateTimeField()

    boutique = forms.EmailField()

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
    s = [("Loi 1901", "Loi 1901"), ("Junior entreprise", "Junior entreprise")]
    statut = forms.MultipleChoiceField(required=True, widget=forms.Select(attrs={
        'class': 'form-control',
        'value': 'Utilisateur'
    }
    ), choices=s)

    members = []
    for m in myUser.objects.all():
        members.append((m.id, m.user.email))
    members.sort(key=lambda tup: tup[1])

    president = forms.MultipleChoiceField(required=True, widget=forms.Select(attrs={
        'class': 'form-control',
        'value': 'Utilisateur'
    }
    ), choices=members)
    vicepresident = forms.MultipleChoiceField(required=True, widget=forms.Select(attrs={
        'class': 'form-control',
        'value': 'Utilisateur'
    }
    ), choices=members)
    tresorier = forms.MultipleChoiceField(required=True, widget=forms.Select(attrs={
        'class': 'form-control',
        'value': 'Utilisateur'
    }
    ), choices=members)
    secretaire = forms.MultipleChoiceField(required=True, widget=forms.Select(attrs={
        'class': 'form-control',
        'value': 'Utilisateur'
    }
    ), choices=members)


class add_member_form(forms.Form):
    members = []
    for m in myUser.objects.all():
        members.append((m.id, m.user.email))
    members.sort(key=lambda tup: tup[1])
    new_member = forms.MultipleChoiceField(required=True, widget=forms.Select(attrs={
        'class': 'form-control',
        'value': 'Utilisateur'
    }
    ), choices=members)

    s = [("Retirer", "Retirer"), ("Président", "Président"), ("Vice-Président", "Vice-Président"),
         ("Trésorier", "Trésorier"),
         ("Secrétaire", "Secrétaire"), ("Membre", "Membre")]
    role = forms.MultipleChoiceField(required=True, widget=forms.Select(attrs={
        'class': 'form-control',
        'value': 'Utilisateur'
    }
    ), choices=s)


class mod_asso(forms.Form):
    description = forms.CharField(initial="", required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    mail = forms.EmailField(initial="", required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    photo = forms.ImageField(initial="", required=True, widget=forms.FileInput(attrs={'type': 'file',
                                                                                      'class': 'form-control'}))
    site = forms.URLField(initial="", required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    s = [("", ""), ("Loi 1901", "Loi 1901"), ("Junior entreprise", "Junior entreprise")]
    statut = forms.MultipleChoiceField(required=False, widget=forms.Select(attrs={
        'class': 'form-control',
        'value': 'Utilisateur'
    }
    ), choices=s)


class modifyUser(forms.Form):
    mail_secondary = forms.EmailField(initial="", required=False,
                                      widget=forms.EmailInput(attrs={'class': 'form-control'}))
    GENDER_OPTIONS = [
        ('', ''),
        ('Male', 'M'),
        ('Female', 'F'),
    ]
    gender = forms.MultipleChoiceField(required=False, widget=forms.Select(attrs={
        'class': 'form-control',
        'value': 'Gender'
    }
    ), choices=GENDER_OPTIONS)


class invite_member_form(forms.Form):
    mail = forms.EmailField(initial="", required=True,
                            widget=forms.EmailInput(attrs={'class': 'form-control'}))
