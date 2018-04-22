from django.db import models


class Event(models.Model):
    association_id = models.ForeignKey('association.Association', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    date_deadline = models.DateTimeField()
    validated = models.BooleanField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # TODO find a better way to store money fields
    place = models.CharField(max_length=100)
    photo = models.ImageField()
    size_intern = models.IntegerField()
    size_extern = models.IntegerField()
    PREMIUM = 'PR'
    PAID = 'PA'
    FREE = 'FR'
    PRIORITY = (
        (PREMIUM, 'Premium'),
        (PAID, 'Payant'),
        (FREE, 'Gratuit'),

    )
    priority = models.CharField(max_length=2, choices=PRIORITY)
    token_staff = models.UUIDField()


class Attend(models.Model):
    user_id = models.ForeignKey('user_settings.User', on_delete=models.DO_NOTHING)
    event_id = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    date_entry = models.DateTimeField()
    ticket_number = models.UUIDField()


class Staff(models.Model):
    user_id = models.ForeignKey('user_settings.User', on_delete=models.DO_NOTHING)
    event_id = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
