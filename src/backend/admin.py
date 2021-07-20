from django.contrib import admin
from django.contrib.admin import register

from backend.models.example import Example
from backend.models.contactsitem import ContactsItem


@register(Example)
class ExampleAdmin(admin.ModelAdmin):
    pass

@register(ContactsItem)
class ContactsItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phonenumber',)


admin.site.register(ContactsItem, ContactsItemAdmin)
