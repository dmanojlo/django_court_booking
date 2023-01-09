from django import forms
from django.forms import ModelForm
from .models import Court, Reservation, Profile
from django.forms.widgets import TimeInput

# class TimePickerInput(forms.TimeInput):
#         input_type = 'time'

import datetime as dt
import time

HOUR_CHOICES = [(dt.time(hour=x, minute=m), '{:02d}:{:02d}'.format(x, m))
                for x in range(9, 20) for m in (0, 30)]
# HOUR_CHOICES = [time(h, m).strftime('%H:%M')
#                 for h in range(9, 17) for m in (0, 30)]


class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'location', 'birth_date')

    def signup(self, request, user):
        # Save your user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        user.profile.location = self.cleaned_data['location']
        user.profile.birth_date = self.cleaned_data['birth_date']
        user.profile.save()


class CourtForm(forms.ModelForm):

    class Meta:
        model = Court
        fields = ('court_name',)


class ReservationForm(forms.ModelForm):
    #with required = False we can disable validation on field
    #court = forms.CharField(required=False)

    class Meta:
        
        model = Reservation
        fields = ('start_time', 'end_time', 'booking_date', 'court')
        widgets = {
            'start_time': forms.TimeInput(format='%H:%M'),
            # 'start_time': TimePickerInput(format='%H:%M'),
            'end_time': forms.Select(choices=HOUR_CHOICES),
            'booking_date': forms.DateInput(format='%d.%m.%Y'),
            #'court': forms.TextInput()
        }
