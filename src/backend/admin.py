from django.contrib import admin
from django.contrib.admin import register

from backend.models.example import Example
from backend.models.article import Article
from backend.models.contact import Contact
from backend.models.faq import Faq
from backend.models.settings import Setting
from backend.models.menu import Menu
from backend.models.project import Project
from backend.models.sponsor import Sponsor
from backend.models.student import Student


@register(Example)
class ExampleAdmin(admin.ModelAdmin):
    pass


@register(Article)
class ArticleItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'published')
    ordering = ['published']


@register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phonenumber', 'subject', 'message')
    ordering = ['name']


@register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'type')
    ordering = ['name']


@register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'published')
    ordering = ['question']


@register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'information', 'facebookURL', 'startDate')


@register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')
    ordering = ['name']


@register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

