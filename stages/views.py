from django.shortcuts import render
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from backend.permissions import IsAdminUser, IsAdminOrReadOnly, IsAdminOrCreateOnly
from .models import OffreStage, DemandeStage
from .serializers import DemandeStageSerializer, OffreStageSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics


@extend_schema_view(
    list=extend_schema(summary="Lister les offres de stage"),
    retrieve=extend_schema(summary="Voir une offre de stage"),
    create=extend_schema(summary="Créer une offre de stage"),
    update=extend_schema(summary="Mettre à jour une offre de stage"),
    partial_update=extend_schema(summary="Mise à jour partielle d'une offre de stage"),
    destroy=extend_schema(summary="Supprimer une offre de stage"),
)
class OffreStageViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour les offres de stage.
    - READ (list, retrieve): Public (AllowAny)
    - CREATE/UPDATE/DELETE: Admin uniquement
    """
    queryset = OffreStage.objects.all()
    serializer_class = OffreStageSerializer
    permission_classes = [IsAdminOrReadOnly]


@extend_schema_view(
    list=extend_schema(summary="Lister les demandes de stage"),
    retrieve=extend_schema(summary="Voir une demande de stage"),
    create=extend_schema(summary="Créer une demande de stage"),
    update=extend_schema(summary="Mettre à jour une demande de stage"),
    partial_update=extend_schema(summary="Mise à jour partielle d'une demande de stage"),
    destroy=extend_schema(summary="Supprimer une demande de stage"),
)
class DemandeStageViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour les demandes de stage.
    - CREATE: Public (AllowAny) - permet aux candidats de postuler
    - READ/UPDATE/DELETE: Admin uniquement
    """
    queryset = DemandeStage.objects.all()
    serializer_class = DemandeStageSerializer
    permission_classes = [IsAdminOrCreateOnly]

    def get_queryset(self):
        """
        Retourne toutes les demandes si l'utilisateur est admin,
        sinon aucune demande (sécurité).
        """
        if self.request.user.is_authenticated:
            try:
                from accounts.models import Administrateur
                if Administrateur.objects.filter(utilisateurs=self.request.user).exists():
                    return DemandeStage.objects.all()
            except Exception:
                pass
        return DemandeStage.objects.none()

    @extend_schema(summary="Mettre à jour le statut d'une demande")
    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        if not request.user.is_staff:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        demande = self.get_object()
        new_status = request.data.get('status')
        if new_status not in dict(DemandeStage.STATUT_CHOICES):
            return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
        demande.statut = new_status
        demande.save()
        serializer = self.get_serializer(demande)
        return Response(serializer.data)


@extend_schema_view(
    get=extend_schema(
        summary="Liste des offres de stage",
        description="Récupère la liste de toutes les offres de stage. Accessible à tous.",
    ),
    post=extend_schema(
        summary="Créer une offre de stage",
        description="Crée une nouvelle offre de stage. Réservé à l'administrateur.",
    ),
)
class OffreStageListCreateView(generics.ListCreateAPIView):
    queryset = OffreStage.objects.all()
    serializer_class = OffreStageSerializer
    permission_classes = [IsAdminOrReadOnly]


@extend_schema_view(
    get=extend_schema(
        summary="Détail d'une offre de stage",
        description="Récupère les informations d'une offre de stage. Accessible à tous.",
    ),
    put=extend_schema(
        summary="Mettre à jour une offre de stage",
        description="Met à jour une offre de stage existante. Réservé à l'administrateur.",
    ),
    patch=extend_schema(
        summary="Mise à jour partielle d'une offre de stage",
        description="Met à jour partiellement une offre de stage existante. Réservé à l'administrateur.",
    ),
    delete=extend_schema(
        summary="Supprimer une offre de stage",
        description="Supprime une offre de stage. Réservé à l'administrateur.",
    ),
)
class OffreStageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OffreStage.objects.all()
    serializer_class = OffreStageSerializer
    permission_classes = [IsAdminOrReadOnly]


@extend_schema_view(
    get=extend_schema(
        summary="Liste des demandes de stage",
        description="Récupère la liste de toutes les demandes de stage. Accessible à tous.",
    ),
    post=extend_schema(
        summary="Créer une demande de stage",
        description="Crée une nouvelle demande de stage. Réservé à l'administrateur.",
    ),
)
class DemandeStageListCreateView(generics.ListCreateAPIView):
    queryset = DemandeStage.objects.all()
    serializer_class = DemandeStageSerializer
    permission_classes = [IsAdminOrReadOnly]


@extend_schema_view(
    get=extend_schema(
        summary="Détail d'une demande de stage",
        description="Récupère les informations d'une demande de stage. Accessible à tous.",
    ),
    put=extend_schema(
        summary="Mettre à jour une demande de stage",
        description="Met à jour une demande de stage existante. Réservé à l'administrateur.",
    ),
    patch=extend_schema(
        summary="Mise à jour partielle d'une demande de stage",
        description="Met à jour partiellement une demande de stage existante. Réservé à l'administrateur.",
    ),
    delete=extend_schema(
        summary="Supprimer une demande de stage",
        description="Supprime une demande de stage. Réservé à l'administrateur.",
    ),
)
class DemandeStageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DemandeStage.objects.all()
    serializer_class = DemandeStageSerializer
    permission_classes = [IsAdminOrReadOnly]
