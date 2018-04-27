from django import forms
from database.models import Association
from django.contrib.auth.models import Group
from django.db.models import DEFERRED

class createEventForm(forms.Form):
    #association_name = forms.CharField(widget=forms.Select(attrs={
    #   'class': 'custom-select',
    #}))

    asso_list = []
    for a in Association.objects.all():
        asso_list.append((a.id, a.name))
    print(asso_list)

    association_name = forms.MultipleChoiceField(required=True, widget=forms.Select(attrs={
        'class': 'form-control',
        'value': 'Association'
    }
                                                                                    ), choices= asso_list)
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
