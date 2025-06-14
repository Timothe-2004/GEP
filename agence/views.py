from rest_framework import generics
from backend.permissions import IsAdminOrReadOnly
from .models import Agence
from .serializers import AgenceSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    get=extend_schema(
        summary="Liste des agences",
        description="Récupère la liste de toutes les agences. Accessible à tous.",
    ),
    post=extend_schema(
        summary="Créer une agence",
        description="Crée une nouvelle agence. Réservé à l'administrateur.",
    ),
)
class AgenceListCreateView(generics.ListCreateAPIView):
    queryset = Agence.objects.all()
    serializer_class = AgenceSerializer
    permission_classes = [IsAdminOrReadOnly]

@extend_schema_view(
    get=extend_schema(
        summary="Détail d'une agence",
        description="Récupère les informations d'une agence. Accessible à tous.",
    ),
    put=extend_schema(
        summary="Mettre à jour une agence",
        description="Met à jour une agence existante. Réservé à l'administrateur.",
    ),
    patch=extend_schema(
        summary="Mise à jour partielle d'une agence",
        description="Met à jour partiellement une agence existante. Réservé à l'administrateur.",
    ),
    delete=extend_schema(
        summary="Supprimer une agence",
        description="Supprime une agence. Réservé à l'administrateur.",
    ),
)
class AgenceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agence.objects.all()
    serializer_class = AgenceSerializer
    permission_classes = [IsAdminOrReadOnly]
