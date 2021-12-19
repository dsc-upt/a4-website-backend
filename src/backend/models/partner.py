from django.db import models

class Partner(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    photo = models.URLField()
    description = models.CharField(max_length=500)
