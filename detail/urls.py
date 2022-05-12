from . import views
from django.urls import path

app_name = 'detail'

urlpatterns = [
    path('', views.show_detail, name='show_detail'),
    path('base/', views.base, name='base'),
    path('tablebase/', views.tablebase, name='table_base'),
    path('imagbase/', views.imag_base, name="imag_base"),

]