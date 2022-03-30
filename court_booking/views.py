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

# Create your views here.

import json

def home(request):
    data = dict()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
    else:
        form = ReservationForm()

    context = {'form':form}
    #data['html_form'] = render_to_string('court_booking/home.html', context, request)
    #return JsonResponse(data)
    return render(request, 'court_booking/home.html', context)
