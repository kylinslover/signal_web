from django.db import models

# Create your models here.


class data(models.Model):
    file_name = models.CharField(max_length=200)
    data_imag_path = models.CharField(max_length=200)
