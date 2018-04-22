from django.db import models
from django.utils import timezone


class Association(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_creation = models.DateTimeField(default=timezone.now)
    mail = models.EmailField(max_length=100)
    photo = models.ImageField()
    site = models.URLField()
    statut = models.CharField(max_length=50)


class Members(models.Model):
    user_id = models.ForeignKey('user_settings.User', on_delete=models.DO_NOTHING)
    association_id = models.ForeignKey(Association, on_delete=models.DO_NOTHING)
    role = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date d'ajout du membre")

    class Meta:
        verbose_name = "Liste des membres des associations"
        ordering = ['id']

    def __str__(self):
        return "{0} fait partie de l'association {1}".format(self.user_id, self.association_id)
