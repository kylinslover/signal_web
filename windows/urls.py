from . import views
from django.urls import path

app_name = 'windows'

urlpatterns = [
    path('', views.show_windows, name='windows'),
]
