from django.db import models
# Django's datetime supports timezones defined in settings.py
from django.utils import timezone

# Create your models here.
# TODO move models to their related Django app.

class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    mail_secondary = models.CharField(max_length=100, blank=True) # Blank is preferred. Do not use null.
    gender = models.NullBooleanField;

    class Meta:
        verbose_name = "Utilisateur"
        ordering = ['id']

    def __str__(self):
        return "{name} {lastname} ({mail})".format(self.firstname, self.lastname, self.mail)

class User(models.Moodel):

class Members(models.Moodel):

class Association(models.Moodel):

class Event(models.Moodel):

class Attend(models.Moodel):

class Staff(models.Moodel):

class SystemAdmin(models.Moodel):

class AssociationsManager(models.Moodel):







