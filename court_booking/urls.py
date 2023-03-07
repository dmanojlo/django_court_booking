from django.urls import path, include
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .views import home, partial_res, index, my_reservations, delete_res
from django.views.generic import TemplateView

app_name = 'court_booking' # za url putanju do appa


urlpatterns = [
     path('index/', index , name='index'),
     path('fullcalendar/', TemplateView.as_view(template_name="fullcalendar.html"), name='fullcalendar'),
     path('book/home/', home , name='home'),
     path('book/home/<int:month>/<int:day>/', home , name='home'),
     path('book/partial_res/', partial_res , name='partial_res'),
     path('my_reservations/', my_reservations , name='my_reservations'),
     path('delete_res/<int:pk>/', delete_res , name='delete_res'),
     ]
