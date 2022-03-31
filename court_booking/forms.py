from django import forms
from django.forms import ModelForm
from .models import Court, Reservation, Profile

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

    class Meta:
        model = Reservation
        fields = ('start_time', 'end_time', 'booking_date', 'court', 'user')