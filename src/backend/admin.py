from django.contrib import admin
from django.contrib.admin import register

from backend.models.example import Example


@register(Example)
class ExampleAdmin(admin.ModelAdmin):
    pass
