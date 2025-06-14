from rest_framework import generics
from backend.permissions import IsAdminOrReadOnly
from .models import Partenaire
from .serializers import PartenaireSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    get=extend_schema(
        summary="Liste des partenaires",
        description="Récupère la liste de tous les partenaires. Accessible à tous.",
    ),
    post=extend_schema(
        summary="Créer un partenaire",
        description="Crée un nouveau partenaire. Réservé à l'administrateur.",
    ),
)
class PartenaireListCreateView(generics.ListCreateAPIView):
    """
    Vue pour lister et créer des partenaires.
    - READ (list): Public (AllowAny)
    - CREATE: Admin uniquement
    """
    queryset = Partenaire.objects.all()
    serializer_class = PartenaireSerializer
    permission_classes = [IsAdminOrReadOnly]

@extend_schema_view(
    get=extend_schema(
        summary="Détail d'un partenaire",
        description="Récupère les informations d'un partenaire. Accessible à tous.",
    ),
    put=extend_schema(
        summary="Mettre à jour un partenaire",
        description="Met à jour un partenaire existant. Réservé à l'administrateur.",
    ),
    patch=extend_schema(
        summary="Mise à jour partielle d'un partenaire",
        description="Met à jour partiellement un partenaire existant. Réservé à l'administrateur.",
    ),
    delete=extend_schema(
        summary="Supprimer un partenaire",
        description="Supprime un partenaire. Réservé à l'administrateur.",
    ),
)
class PartenaireRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vue pour récupérer, modifier et supprimer un partenaire.
    - READ (retrieve): Public (AllowAny)
    - UPDATE/DELETE: Admin uniquement
    """
    queryset = Partenaire.objects.all()
    serializer_class = PartenaireSerializer
    permission_classes = [IsAdminOrReadOnly]
