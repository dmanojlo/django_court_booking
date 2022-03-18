from django.urls import path, include
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .views import home


app_name = 'court_booking' # za url putanju do appa

urlpatterns = [
     path('home/', home , name='home'),
     ]
