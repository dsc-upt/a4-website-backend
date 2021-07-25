from django.db import models


class Settings(models.Model):
    TYPES = {
        ("TEXT", "Text"),
        ("IMAGE", "Image")
    }


    name = models.CharField(max_length=500, default = '')
    value = models.TextField(max_length=300, blank=True, default='')
    type = models.CharField(max_length=5, choices=TYPES, default='TEXT')
