from . import views
from django.urls import path

app_name = 'filter'

urlpatterns = [
    path('', views.show_fileter, name='fileter'),
]