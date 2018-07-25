from django import forms
from django.core.exceptions import ValidationError

def c_gender():
    BLANK = "---"
    MASCULINO = 'Masculino'
    FEMENINO = 'Feminino'
    gender_list = ((BLANK, '---'), (MASCULINO, 'Masculino'), (FEMENINO, 'Feminino'))
    return gender_list

def c_designation():
    BLANK = "---"
    ANCIAO = 'Ancião'
    SER_MIN = 'Servo Ministerial'
    PUBLIC = 'Publicador'
    BAP = 'Irmão Batizado'
    designation_list = ((BLANK, '---'), (ANCIAO, 'Ancião'), (SER_MIN, 'Servo Ministerial'),(BAP, 'Irmão Batizado'), (PUBLIC, 'Publicador'))
    return designation_list

def c_car():
    BLANK = "---"
    SIM = 'Sim'
    NAO = 'Não'
    c_list = ((BLANK, '---'), (SIM, 'Sim'), (NAO, 'Não'))
    return c_list

def validar_tel(value):
    """Validar que o campo fique telefone tenha apenas numeros e 11 digitos"""
    if not value.isdigit():
        raise ValidationError('Apenas números no cadastro do telefone')
    if len(value) != 11:
        raise ValidationError('Telefone deve conter 11 digitos. Ex: 31999998888')

class CadastroForm(forms.Form):
    nome = forms.CharField(label='Nome', widget=forms.TextInput(
        attrs={
            'class': 'form-control-1',
            'placeholder': 'Escreva um nome aqui...'
        }
    ))
    endereco = forms.CharField(label='Endereço', required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control-1',
            'placeholder': 'Escreva um endereço aqui...'
        }
    ))
    telefone = forms.CharField(label='Telefone', required=False, validators=[validar_tel], widget=forms.TextInput(
        attrs={
            'class': 'form-control-1',
            'placeholder': 'Escreva um telefone aqui...'
        }
    ))
    sexo = forms.ChoiceField(label='Sexo', choices=c_gender(), widget=forms.Select(
        attrs={
            'class':'form-control-1'
        }
    ))
    designacao = forms.ChoiceField(label='Designação', choices=c_designation(), widget=forms.Select(
        attrs={
            'class':'form-control-1'
        }
    ))
    carrinho = forms.ChoiceField(label='Carrinho', choices=c_car(), widget=forms.Select(
        attrs={
            'class':'form-control-1'
        }
    ))

    def clean_nome(self):
        """Padronizar nomes"""
        nome = self.cleaned_data['nome']
        words = [w.capitalize() for w in nome.split()]
        return ' '.join(words)
