from django.db import models
from django.conf import settings
# Create your models here.

class Court(models.Model):
    court_name = models.CharField(max_length=200)

class Reservation(models.Model):
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    booking_date = models.DateField(auto_now=False, auto_now_add=False)
    court = models.ForeignKey(Court, on_delete=models.CASCADE, related_name='reservation')
    #user_id = models.ForeignKey()
