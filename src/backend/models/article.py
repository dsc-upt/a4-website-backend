from django.db import models

#add slug and image
class Article(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, primary_key=True, blank=True, null=True)
    content = models.TextField()
    published = models.BooleanField()
