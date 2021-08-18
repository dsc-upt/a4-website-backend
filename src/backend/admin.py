from django.contrib import admin
from django.contrib.admin import register

from backend.models.example import Example
from backend.models.settings import Settings

from backend.models.faqitem import FAQItem


@register(Example)
class ExampleAdmin(admin.ModelAdmin):
    pass


@register(Settings)
class ExampleSettings(admin.ModelAdmin):
    pass


@register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'publish_date')
    ordering = ['publish_date']
