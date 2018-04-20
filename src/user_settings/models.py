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


class Members(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    association_id = models.ForeignKey(Association, on_delete=models.DO_NOTHING)
    role = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(default=timezone.now(), verbose_name="Date d'ajout du membre")

    class Meta:
        verbose_name = "Liste des membres des associations"
        ordering = ['id']

    def __str__(self):
        return "{name} fait partie de l'association {asso}".format(self.user_id, self.association_id)

class Association(models.Model):

class Event(models.Model):

class Attend(models.Model):

class Staff(models.Model):

class SystemAdmin(models.Model):

class AssociationsManager(models.Model):







