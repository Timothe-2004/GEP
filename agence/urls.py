from django.urls import path
from .views import AgenceListCreateView, AgenceRetrieveUpdateDestroyView

urlpatterns = [
    path('', AgenceListCreateView.as_view(), name='agence-list-create'),
    path('<int:pk>/', AgenceRetrieveUpdateDestroyView.as_view(), name='agence-detail'),
]
