from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    subject = models.CharField(max_length = 128)
    message = models.TextField()