from django.db import models

# Create your models here.
class Curso(models.Model):
    binbre = models.CharField(max_length=30)
    credito = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.binbre, self.credito)