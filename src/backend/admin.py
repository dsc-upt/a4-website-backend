from django.contrib import admin
from django.contrib.admin import register

from backend.models.example import Example
from backend.models.faq import Faq
from backend.models.settings import Settings


@register(Example)
class ExampleAdmin(admin.ModelAdmin):
    pass


@register(Settings)
class ExampleSettings(admin.ModelAdmin):
    pass


@register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'published')
    ordering = ['question']