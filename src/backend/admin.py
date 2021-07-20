from django.contrib import admin
from django.contrib.admin import register

from backend.models.example import Example
from backend.models.contactsitem import ContactsItem


@register(Example)
@register(ContactsItem)
class ExampleAdmin(admin.ModelAdmin):
    pass

class ContactsItemAdmin(admin.ModelAdmin):
    search_fields = ('name', 'surname', 'email', 'phonenumber')

admin.site.register(ContactsItem, ContactsItemAdmin)
