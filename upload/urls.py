from . import views
from django.urls import path

app_name = 'upload'

urlpatterns = [
    path('', views.upload, name='upload'),
]