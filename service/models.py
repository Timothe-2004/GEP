from django.db import models

class Service(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='service/icons/', blank=True, null=True)

    def __str__(self):
        return self.nom
