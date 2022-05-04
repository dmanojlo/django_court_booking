from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required #for function based views
from django.contrib.auth.mixins import LoginRequiredMixin #for classed based views
from django.db.models import F #F() expressions are good for memory
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.db import transaction
from django.core.cache import cache

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Reservation, Court
from .forms import ReservationForm, SignupForm, CourtForm
import calendar
from calendar import HTMLCalendar
from datetime import date

# Create your views here.

import json

def home(request, month, day):
    data = dict()
    #used to get a list of  single field in model
    courts = list(Court.objects.values_list('court_name', flat=True))
    name = 'Pero'
    # year = date.today().year
    # month = date.today().month
    # cal = HTMLCalendar().formatmonth(year, month)

    # if request.method == 'POST':
    #     form = ReservationForm(request.POST)
    # else:
    #     form = ReservationForm()
    context = {'courts':courts,'name':name}
    #data['html_form'] = render_to_string('court_booking/home.html', context, request)
    #return JsonResponse(data)
    book_date = Reservation.objects.filter(booking_date__day=day)
    print(book_date)
    if day == 6:
        return render(request, 'court_booking/home.html', context)
    else:
        return render(request, 'court_booking/home.html', context)

def partial_res(request):
    data = dict()
    if request.method == 'POST':
        # court_nam = request.POST.get('court')
        # print(court_nam)
        # court = Court.objects.get(court_name=court_nam)
        # print(court)
        form = ReservationForm(request.POST)
        #if form.is_valid():
        print('ndjanddsknsf')
        res = form.save(commit=False)
        print(res)
        res.user = request.user
        res.save()
        data['html_form'] = render_to_string('court_booking/partial_reservation_form.html', {'form': form}, request)

    else:
        form = ReservationForm()
    context = {'form':form}
    data['html_form'] = render_to_string('court_booking/partial_reservation_form.html', context, request)
    return JsonResponse(data)
