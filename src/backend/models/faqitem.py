from django.db import models


class FAQItem(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    publish_date = models.DateField()

    def __str__(self):
        return self.question
