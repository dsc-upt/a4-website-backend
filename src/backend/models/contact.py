from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phonenumber = models.IntegerField(max_length=10)