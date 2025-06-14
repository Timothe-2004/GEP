from rest_framework import serializers
from .models import Article, Categorie

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'nom']

class ArticleSerializer(serializers.ModelSerializer):
    categorie = CategorieSerializer()

    class Meta:
        model = Article
        fields = '__all__'

    def create(self, validated_data):
        categorie_data = validated_data.pop('categorie')
        categorie, created = Categorie.objects.get_or_create(nom=categorie_data['nom'])
        article = Article.objects.create(categorie=categorie, **validated_data)
        return article
