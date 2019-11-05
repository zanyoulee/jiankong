
from django.db import models

# Create your models here.
# Create your models here.
from rest_framework import serializers


class book_zhoudu(models.Model):
    id = models.IntegerField(max_length=11,auto_created=True,primary_key=True)
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    fenlei = models.CharField(max_length=64)
    score = models.CharField(max_length=64)
    dwlink1 = models.CharField(max_length=255)
    dwlink2 = models.CharField(max_length=255)
    dwlink3 = models.CharField(max_length=255)



