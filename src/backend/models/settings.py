from django.db import models


class Setting(models.Model):
    TYPES = {
        ("TEXT", "Text"),
        ("IMAGE", "Image")
    }

    slug = models.SlugField(primary_key=True, null=True)
    name = models.CharField(max_length=500)
    value = models.TextField(max_length=300)
    type = models.CharField(max_length=5, choices=TYPES, default='TEXT')
