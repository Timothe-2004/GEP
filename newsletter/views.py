from rest_framework import generics
from backend.permissions import IsAdminOrReadOnly
from .models import NewsletterAbonne
from .serializers import NewsletterAbonneSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    post=extend_schema(
        summary="S'abonner à la newsletter",
        description="Permet à un utilisateur de s'abonner à la newsletter. Accessible à tous.",
    ),
)
class NewsletterAbonneCreateView(generics.CreateAPIView):
    queryset = NewsletterAbonne.objects.all()
    serializer_class = NewsletterAbonneSerializer
    permission_classes = [IsAdminOrReadOnly]

@extend_schema_view(
    get=extend_schema(
        summary="Liste des abonnés à la newsletter",
        description="Récupère la liste de tous les abonnés à la newsletter. Réservé à l'administrateur.",
    ),
)
class NewsletterAbonneListView(generics.ListAPIView):
    queryset = NewsletterAbonne.objects.all()
    serializer_class = NewsletterAbonneSerializer
    permission_classes = [IsAdminOrReadOnly]
