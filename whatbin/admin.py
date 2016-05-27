from django.contrib import admin
from whatbin.models import Bin, Item


@admin.register(Bin)
class BinAdmin(admin.ModelAdmin):
    list_display = ['title']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['title', ]
        else:
            return []


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['title', ]
        else:
            return []