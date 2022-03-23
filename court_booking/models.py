from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Court(models.Model):
    court_name = models.CharField(max_length=200)

    def __str__(self):
        return self.court_name

class Reservation(models.Model):
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    booking_date = models.DateField(auto_now=False, auto_now_add=False)
    court = models.ForeignKey(Court, on_delete=models.CASCADE, related_name='court_reservation')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_reservation')

    def __str__(self):
        return self.user
