from django.db import models
from django.core.exceptions import ValidationError

def c_gender():
    MASCULINO = 'Masculino'
    FEMENINO = 'Feminino'
    gender_list = ((MASCULINO, 'Masculino'), (FEMENINO, 'Feminino'))
    return gender_list

def c_designation():
    ANCIAO = 'Ancião'
    SER_MIN = 'Servo Ministerial'
    PUBLIC = 'Publicador'
    BAP = 'Irmão Batizado'
    designation_list = ((ANCIAO, 'Ancião'), (SER_MIN, 'Servo Ministerial'), (BAP, 'Irmão Batizado'), (PUBLIC, 'Publicador'))
    return designation_list

def c_car():
    SIM = 'Sim'
    NAO = 'Não'
    c_list = ((SIM, 'Sim'), (NAO, 'Não'))
    return c_list

def validar_tel(value):
    """Validar que o campo fique telefone tenha apenas numeros e 11 digitos"""
    if not value.isdigit():
        raise ValidationError('Apenas números no cadastro do telefone')
    if len(value) != 11:
        raise ValidationError('Telefone deve conter 11 digitos. Ex: 31999998888')

class Cadastro(models.Model):
    nome = models.CharField('nome', max_length=100)
    endereco = models.CharField('endereço', max_length=100)
    telefone = models.CharField('telefone', max_length=20, validators=[validar_tel])
    sexo = models.CharField('sexo', max_length=30, choices=c_gender())
    designacao = models.CharField('designacao', max_length=30, choices=c_designation())
    carrinho = models.CharField('carrinho', max_length=30, choices=c_car())
    created_at = models.DateTimeField('criado em', auto_now_add=True)
   
    class Meta:
        verbose_name_plural = 'cadastros'
        verbose_name = 'cadastro'
    
    def __str__(self):
        return self.nome


