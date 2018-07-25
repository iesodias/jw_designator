from django.db import models


def a_list():
    SIM = 'Sim'
    NAO = 'Não'
    a_list = ((SIM, 'Sim'), (NAO, 'Não'))
    return a_list

def score():
    T = 'A+'
    A = 'A'
    B = 'B'
    C = 'C'
    score = ((T, 'A+'), (A, 'A'), (B, 'B'), (C, 'C'))
    return score

class Oradores(models.Model):
    nome = models.CharField('Nome', max_length=100)
    contato = models.CharField('Telefone', max_length=100)
    congregacao = models.CharField('Congregação', max_length=100)
    tema = models.CharField('Tema', max_length=100)
    email = models.EmailField('e-mail')
    dia = models.CharField('Dia', max_length=100)
    data = models.DateField(unique=True)
    horario = models.TimeField()
    ajuda = models.CharField('Ajuda', max_length=100, choices=a_list())
    custo = models.CharField('Custo', max_length=100)
    nota = models.CharField('Nota', max_length=100, choices=score())

    class Meta:
        verbose_name_plural = 'oradores'
        verbose_name = 'orador'

    def __str__(self):
        return self.nome


