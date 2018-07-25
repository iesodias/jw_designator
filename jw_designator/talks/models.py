from django.db import models

class Temas(models.Model):
    tema = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'temas'
        verbose_name = 'tema'

    def __str__(self):
        return self.tema
