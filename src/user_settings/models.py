from django.db import models
# Django's datetime supports timezones defined in settings.py
from django.utils import timezone

# Create your models here.
# TODO move models to their related Django app.

class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    mail_secondary = models.EmailField(max_length=100, blank=True) # Blank is preferred. Do not use null.
    MALE = 'M'
    FEMALE = 'F'
    NON_BINARY = 'N'
    GENDER_CHOICES = (
        (MALE, 'Homme'),
        (FEMALE, 'Femme'),
        (NON_BINARY, 'Non binaire'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        verbose_name = "Utilisateur"
        ordering = ['id']

    def __str__(self):
        return "{0} {1} ({2})".format(self.firstname, self.lastname, self.mail)


class Members(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    association_id = models.ForeignKey(Association, on_delete=models.DO_NOTHING)
    role = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(default=timezone.now(), verbose_name="Date d'ajout du membre")

    class Meta:
        verbose_name = "Liste des membres des associations"
        ordering = ['id']

    def __str__(self):
        return "{0} fait partie de l'association {1}".format(self.user_id, self.association_id)

class Association(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_creation = models.DateTimeField(default=timezone.now())
    mail = models.EmailField(max_length=100)
    photo = models.ImageField()
    site = models.URLField()

class Event(models.Model):
    association_id = models.ForeignKey(Association, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    validated = models.BooleanField()
    description = models.TextField(blank=True)
    price = models.

class Attend(models.Model):

class Staff(models.Model):

class SystemAdmin(models.Model):

class AssociationsManager(models.Model):







