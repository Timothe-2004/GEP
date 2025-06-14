from django.urls import path
from .views import (
    ArticleListCreateView, ArticleRetrieveUpdateDestroyView, CategorieListCreateView, articles_by_categorie
)

urlpatterns = [
    path('articles/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleRetrieveUpdateDestroyView.as_view(), name='article-detail'),
    path('categories/', CategorieListCreateView.as_view(), name='categorie-list-create'),
    path('categories/<int:categorie_id>/articles/', articles_by_categorie, name='articles-by-categorie'),
]
