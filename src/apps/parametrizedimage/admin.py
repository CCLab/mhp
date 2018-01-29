from django.contrib import admin

from src.apps.parametrizedimage.models import CardImage, CARD_PARAMETERS


class CardImageAdmin(admin.ModelAdmin):
    list_display = [parameter['parameter_name'] for parameter in CARD_PARAMETERS if parameter['type'] != 'tags']


admin.site.register(CardImage, CardImageAdmin)
