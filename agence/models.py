from django.db import models

class Agence(models.Model):
    ville = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    telephone = models.CharField(max_length=30)
    image = models.ImageField(upload_to='agences/images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.ville} - {self.quartier}"
