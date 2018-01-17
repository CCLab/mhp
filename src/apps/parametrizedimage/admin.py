from django.contrib import admin

from src.apps.parametrizedimage.models import Card, CARD_PARAMETERS


class CardAdmin(admin.ModelAdmin):
    list_display = [parameter['parameter_name'] for parameter in CARD_PARAMETERS]


admin.site.register(Card, CardAdmin)
