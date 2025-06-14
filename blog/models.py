from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class Article(models.Model):
    titre = models.CharField(max_length=255)
    sous_titre = models.CharField(max_length=255)
    corps = models.TextField()
    image_principale = models.ImageField(upload_to='blog/main/', blank=True, null=True)
    images_secondaires = models.ImageField(upload_to='blog/secondary/', blank=True, null=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.titre
