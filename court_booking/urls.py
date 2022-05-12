from django.urls import path, include
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .views import home, partial_res

app_name = 'court_booking' # za url putanju do appa


urlpatterns = [
     path('book/home/<int:month>/<int:day>/', home , name='home'),
     path('book/partial_res/', partial_res , name='partial_res'),
     ]
