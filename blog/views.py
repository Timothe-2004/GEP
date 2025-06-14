from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from backend.permissions import IsAdminOrReadOnly
from .models import Article, Categorie
from .serializers import ArticleSerializer, CategorieSerializer
from django.core.mail import send_mail
from newsletter.models import NewsletterAbonne
from django.conf import settings
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    get=extend_schema(
        summary="Liste des articles de blog",
        description="Récupère la liste de tous les articles de blog. Accessible à tous.",
    ),
    post=extend_schema(
        summary="Créer un article de blog",
        description="Crée un nouvel article de blog. Réservé à l'administrateur.",
    ),
)
class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        article = serializer.save()
        # Envoi de l'article aux abonnés
        abonnés = NewsletterAbonne.objects.all()
        for abonne in abonnés:
            send_mail(
                subject=f"Nouveau blog: {article.titre}",
                message=article.corps[:200],
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[abonne.email],
                fail_silently=True,
            )

@extend_schema_view(
    get=extend_schema(
        summary="Détail d'un article de blog",
        description="Récupère les informations d'un article de blog. Accessible à tous.",
    ),
    put=extend_schema(
        summary="Mettre à jour un article de blog",
        description="Met à jour un article de blog existant. Réservé à l'administrateur.",
    ),
    patch=extend_schema(
        summary="Mise à jour partielle d'un article de blog",
        description="Met à jour partiellement un article de blog existant. Réservé à l'administrateur.",
    ),
    delete=extend_schema(
        summary="Supprimer un article de blog",
        description="Supprime un article de blog. Réservé à l'administrateur.",
    ),
)
class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminOrReadOnly]

@extend_schema_view(
    get=extend_schema(
        summary="Liste des catégories de blog",
        description="Récupère la liste de toutes les catégories de blog. Accessible à tous.",
    ),
    post=extend_schema(
        summary="Créer une catégorie de blog",
        description="Crée une nouvelle catégorie de blog. Réservé à l'administrateur.",
    ),
)
class CategorieListCreateView(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [IsAdminOrReadOnly]

@extend_schema(
    summary="Articles par catégorie",
    description="Récupère tous les articles d'une catégorie donnée. Accessible à tous.",
)
@api_view(['GET'])
@permission_classes([AllowAny])
def articles_by_categorie(request, categorie_id):
    articles = Article.objects.filter(categorie_id=categorie_id)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
