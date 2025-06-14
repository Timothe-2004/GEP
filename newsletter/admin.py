from django.contrib import admin
from .models import NewsletterAbonne

@admin.register(NewsletterAbonne)
class NewsletterAbonneAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'date_abonnement')
    search_fields = ('nom', 'prenom', 'email')
    readonly_fields = ('date_abonnement',)
