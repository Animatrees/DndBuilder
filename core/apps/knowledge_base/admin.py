from django.contrib import admin
from .models import Characteristic


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title',)
    ordering = ('title',)
