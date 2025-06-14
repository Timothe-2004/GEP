from django.contrib import admin
from .models import Agence

@admin.register(Agence)
class AgenceAdmin(admin.ModelAdmin):
    list_display = ('ville', 'quartier', 'telephone')
    search_fields = ('ville', 'quartier', 'telephone')
