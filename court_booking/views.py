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
from django.db.models import F
# Create your views here.

import json


def index(request):
    return render(request, 'court_booking/index.html', {})

@login_required(login_url='account_login')
#we need to set default arguments to go to current month and day
def home(request, month=date.today().month, day=date.today().day):
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
    #data['html_form'] = render_to_string('court_booking/home.html', context, request)
    #return JsonResponse(data)
    book_date = list(Reservation.objects.filter(booking_date__day=day, booking_date__month=month).values('start_time', 'end_time', 'court__court_name'))
    md = [month, day]
    print(md)
    context = {'courts':courts,'name':name, 'book_date':book_date, 'md':md}
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


def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    context = {'reservations': reservations}
    return render(request, 'court_booking/my_reservations.html', context)

def delete_res(request,pk):
    res = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        res.delete()
        return redirect('court_booking:my_reservations')
    return render(request, 'court_booking/delete.html', {'obj':res})