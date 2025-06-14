from django.contrib import admin
from .models import Article, Categorie
from newsletter.models import NewsletterAbonne
from django.core.mail import send_mail
from django.conf import settings

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'date_publication')
    search_fields = ('titre', 'sous_titre', 'corps')
    list_filter = ('categorie', 'date_publication')
    actions = ['envoyer_aux_abonnes']

    def envoyer_aux_abonnes(self, request, queryset):
        abonnés = NewsletterAbonne.objects.all()
        for article in queryset:
            for abonne in abonnés:
                send_mail(
                    subject=f"Nouveau blog: {article.titre}",
                    message=article.corps[:200],
                    from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', None),
                    recipient_list=[abonne.email],
                    fail_silently=True,
                )
        self.message_user(request, "Article(s) envoyé(s) aux abonnés.")
    envoyer_aux_abonnes.short_description = "Transférer l'article aux abonnés"

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)
