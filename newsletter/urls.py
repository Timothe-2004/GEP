from django.urls import path
from .views import NewsletterAbonneCreateView, NewsletterAbonneListView

urlpatterns = [
    path('subscribe/', NewsletterAbonneCreateView.as_view(), name='newsletter-subscribe'),
    path('abonnes/', NewsletterAbonneListView.as_view(), name='newsletter-abonnes'),
]
