from rest_framework import serializers
from .models import NewsletterAbonne

class NewsletterAbonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterAbonne
        fields = '__all__'
        read_only_fields = ['date_abonnement']
