from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class myUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mail_secondary = models.EmailField(max_length=100, blank=True)  # Blank is preferred. Do not use null.
    MALE = 'M'
    FEMALE = 'F'
    NON_BINARY = 'N'
    GENDER_CHOICES = (
        (MALE, 'Homme'),
        (FEMALE, 'Femme'),
        (NON_BINARY, 'Non binaire'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    class Meta:
        verbose_name = "Utilisateur"
        ordering = ['id']

    def __str__(self):
        return "{0} {1} ({2})".format(self.user.first_name, self.user.last_name, self.user.email)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            myUser.objects.create(user=instance)

    #@receiver(post_save, sender=User)
    #def save_user_profile(sender, instance, **kwargs):
    #    myUser.objects.get(user=User)

class SystemAdmin(models.Model):
    user_id = models.ForeignKey(myUser, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return "{0} {1} ({2})".format(self.user_id.first_name, self.user_id.last_name, self.user_id.email)


class AssociationsManager(models.Model):
    user_id = models.ForeignKey(myUser, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return "{0} {1} ({2})".format(self.user_id.first_name, self.user_id.last_name, self.user_id.email)


class Association(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_creation = models.DateTimeField(default=timezone.now)
    mail = models.EmailField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='associations', blank=True)
    site = models.URLField(blank=True)
    statut = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.name)


class Members(models.Model):
    user_id = models.ForeignKey(myUser, on_delete=models.DO_NOTHING)
    association_id = models.ForeignKey(Association, on_delete=models.DO_NOTHING)
    role = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date d'ajout du membre")

    class Meta:
        verbose_name = "Liste des membres des associations"
        ordering = ['id']

    def __str__(self):
        return "{0} fait partie de l'association {1}".format(self.user_id, self.association_id)


class Event(models.Model):
    association_id = models.ForeignKey(Association, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    date_deadline = models.DateTimeField()
    validated = models.BooleanField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # TODO find a better way to store money fields
    place = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='event', blank=True)
    size_intern = models.IntegerField()
    size_extern = models.IntegerField()
    premium = models.NullBooleanField()
    token_staff = models.CharField(max_length=100)

    def __str__(self):
        return "{0} par {1}".format(self.title, self.association_id.name)


class Attend(models.Model):
    user_id = models.ForeignKey(myUser, on_delete=models.DO_NOTHING)
    event_id = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    date_entry = models.DateTimeField()
    ticket_number = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "{0] {1} participe à {2}".format(self.user_id.user.first_name, self.user_id.user.last_name,
                                                self.event_id.title)


class Staff(models.Model):
    user_id = models.ForeignKey(myUser, on_delete=models.DO_NOTHING)
    event_id = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self):
        return "{0} {1} staff {2}".format(self.user_id.user.first_name, self.user_id.user.last_name,
                                          self.event_id.title)
