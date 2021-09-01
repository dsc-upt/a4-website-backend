from django.db import models


class ArticleItem(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
