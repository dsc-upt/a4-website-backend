from django.db import models


class Sponsor(models.Model):
    name = models.CharField(max_length=150)
    image = models.URLField()
    description = models.TextField()
    slug = models.SlugField(max_length=250,
                            primary_key=True,
                            blank=True)
