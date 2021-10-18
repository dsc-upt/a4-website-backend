from django.contrib import admin
from django.contrib.admin import register

from backend.models.example import Example
from backend.models.article import Article
from backend.models.contact import Contact
from backend.models.faq import Faq
from backend.models.settings import Setting


@register(Example)
class ExampleAdmin(admin.ModelAdmin):
    pass

@register(Article)
class ArticleItemsAdmin(admin.ModelAdmin):
    pass

@register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phonenumber', 'subject', 'message')
    oredering = ['name']


@register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'type')
    ordering = ['name']


@register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'published')
    ordering = ['question']