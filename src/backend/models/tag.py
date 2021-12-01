from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250, primary_key=True, blank=True)