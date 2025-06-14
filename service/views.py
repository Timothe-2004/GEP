from rest_framework import generics
from backend.permissions import IsAdminOrReadOnly
from .models import Service
from .serializers import ServiceSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    get=extend_schema(
        summary="Liste des services",
        description="Récupère la liste de tous les services disponibles. Accessible à tous.",
    ),
    post=extend_schema(
        summary="Créer un service",
        description="Crée un nouveau service. Réservé à l'administrateur.",
    ),
)
class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]

@extend_schema_view(
    get=extend_schema(
        summary="Détail d'un service",
        description="Récupère les informations d'un service. Accessible à tous.",
    ),
    put=extend_schema(
        summary="Mettre à jour un service",
        description="Met à jour un service existant. Réservé à l'administrateur.",
    ),
    patch=extend_schema(
        summary="Mise à jour partielle d'un service",
        description="Met à jour partiellement un service existant. Réservé à l'administrateur.",
    ),
    delete=extend_schema(
        summary="Supprimer un service",
        description="Supprime un service. Réservé à l'administrateur.",
    ),
)
class ServiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]
