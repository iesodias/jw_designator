from django.db import models

def c_grupos():
    #Função para padronizar os nomes, e aparecer o choicefield tanto no "admin do django" como no "formulario" de cadastro
    grupo1 = 'Grupo 1'
    grupo2 = 'Grupo 2'
    grupo3 = 'Grupo 3'
    grupo4 = 'Grupo 4'
    grupo5 = 'Grupo 5'
    grupos_lista = ((grupo1, 'Grupo1'), (grupo2, 'Grupo2'), (grupo3, 'Grupo3'), (grupo3, 'Grupo3'), (grupo4, 'Grupo4'), (grupo5, 'Grupo5'))
    return grupos_lista

class Grupo(models.Model):
    grupo = models.CharField('Grupo', max_length=100, choices=c_grupos())
    nome = models.CharField('Nome', max_length=100)
    endereco = models.CharField('Endereço', max_length=100)
    sup_grupo = models.CharField('Sup_grupo', max_length=100)

    class Meta:
        verbose_name_plural = 'grupos'
        verbose_name = 'grupo'
    
    def __str__(self):
        return self.grupo


    