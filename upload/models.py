from django.db import models


# Create your models here.


class UffFile(models.Model):
    file_path = models.CharField(max_length=200)
    file_name = models.CharField(max_length=200)
    upload_time = models.TimeField()
