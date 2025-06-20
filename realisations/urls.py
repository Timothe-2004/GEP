from django.urls import path
from .views import (
    RealisationListCreateView,
    RealisationRetrieveUpdateDestroyView,
    RealisationCreateView,
    RealisationUpdateView,
    RealisationDeleteView,
    liste_categories
)

app_name = 'realisations'

urlpatterns = [
    # API de liste et de filtre des réalisations
    path('', RealisationListCreateView.as_view(), name='list'),
    
    # API de détail d'une réalisation + update/delete
    path('<int:pk>/', RealisationRetrieveUpdateDestroyView.as_view(), name='detail'),
    
    # API de création d'une réalisation (admin uniquement)
    path('create/', RealisationCreateView.as_view(), name='realisation-create'),
    
    # API de mise à jour d'une réalisation (admin uniquement)
    path('<int:pk>/update/', RealisationUpdateView.as_view(), name='realisation-update'),
    
    # API de suppression d'une réalisation (admin uniquement)
    path('<int:pk>/delete/', RealisationDeleteView.as_view(), name='realisation-delete'),
    
    # API pour obtenir la liste des catégories
    path('categories/', liste_categories, name='categorie-list'),
]