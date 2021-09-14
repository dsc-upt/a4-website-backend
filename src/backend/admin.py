from django.contrib import admin
from django.contrib.admin import register

from backend.models.example import Example
from backend.models.settings import Settings
from backend.models.article import Article


@register(Example)
class ExampleAdmin(admin.ModelAdmin):
    pass

@register(Settings)
class ExampleSettings(admin.ModelAdmin):
    pass

@register(Article)
class ArticleItemsAdmin(admin.ModelAdmin):
    pass