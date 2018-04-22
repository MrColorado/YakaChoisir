from django.db import models
# Django's datetime supports timezones defined in settings.py


# TODO move models to their related Django app.
class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    mail_secondary = models.EmailField(max_length=100, blank=True)  # Blank is preferred. Do not use null.
    MALE = 'M'
    FEMALE = 'F'
    NON_BINARY = 'N'
    GENDER_CHOICES = (
        (MALE, 'Homme'),
        (FEMALE, 'Femme'),
        (NON_BINARY, 'Non binaire'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    inscription_date = models.DateTimeField()
    is_intern = models.BooleanField()

    class Meta:
        verbose_name = "Utilisateur"
        ordering = ['id']

    def __str__(self):
        return "{0} {1} ({2})".format(self.firstname, self.lastname, self.mail)


class SystemAdmin(models.Model):
    user_id = models.CharField(max_length=100)


class AssociationsManager(models.Model):
    user_id = models.CharField(max_length=100)
