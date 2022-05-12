from . import views
from django.urls import path

app_name = 'time_domain'

urlpatterns = [
    path('', views.time_domain, name='time_domain'),
]