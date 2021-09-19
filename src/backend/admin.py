from django.contrib import admin
from django.contrib.admin import register

from backend.models.example import Example
from backend.models.contact import Contact


@register(Example)
class ExampleAdmin(admin.ModelAdmin):
    pass


@register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phonenumber',)
    oredering = ['name']
