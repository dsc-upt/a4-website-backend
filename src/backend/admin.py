from django.contrib import admin
from django.contrib.admin import register

from backend.models.example import Example
from backend.models.settings import Settings
from backend.models.ArticleItem import ArticleItem


@register(Example)
class ExampleAdmin(admin.ModelAdmin):
    pass

@register(Settings)
class ExampleSettings(admin.ModelAdmin):
    pass

@register(ArticleItem)
class ArticleItemsAdmin(admin.ModelAdmin):
    pass