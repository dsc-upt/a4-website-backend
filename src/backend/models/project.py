from django.db import models


# name, information, facebook url, starting date, and a list of sponsors (objects from the Sponsor model)

class Project(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    information = models.CharField(max_length=1000)
    facebookURL = models.URLField()
    startDate = models.DateField()
    # sponsors = ArrayField( )
