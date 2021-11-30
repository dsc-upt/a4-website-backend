from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=500)
    link = models.URLField()

    class MenuType(models.TextChoices):
        EXTERNAL_LINK = 'EXTERNAL'
        INTERNAL_LINK = 'INTERNAL'
        SCROLL_TO = 'SCROLL'

    type = models.CharField(
        max_length=9,
        choices=MenuType.choices,
        default=MenuType.INTERNAL_LINK,
    )

    parent = models.ForeignKey('Menu', on_delete = models.CASCADE, blank = True, null = True)
    icon = models.URLField(blank = True, null = True)
