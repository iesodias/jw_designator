from django import forms
from jw_designator.talks.models import Temas
from jw_designator.discursos.models import Oradores
from django.core.exceptions import ValidationError

def a_list():
    BLANK = "---"
    SIM = 'Sim'
    NAO = 'Não'
    a_list = ((BLANK, '---'), (SIM, 'Sim'), (NAO, 'Não'))
    return a_list

def score():
    BLANK = "---"
    A = 'A'
    B = 'B'
    C = 'C'
    score = ((BLANK, '---'), (A, 'A'), (B, 'B'), (C, 'C'))
    return score


class DiscursoForm(forms.Form):
    
    #def  clean_date(self):
    #    data = super(DiscursoForm, self).clean()
    #    dt = data.get('data')
    #    if Oradores.objects.filter(data=dt).exists():
    #        raise forms.ValidationError("Data ja existente")
    #    return dt

    nome = forms.CharField(label='Nome', widget=forms.TextInput(
        attrs={
            'class': 'form-control-1',
            'placeholder': 'Escreva um nome aqui...'
        }
    ))

    contato = forms.CharField(label='Nome', widget=forms.TextInput(
        attrs={
            'class': 'form-control-1',
            'placeholder': 'Telefone de contato'
        }
    ))

    congregacao = forms.CharField(label='Nome', widget=forms.TextInput(
        attrs={
            'class': 'form-control-1',
            'placeholder': 'Digite o nome da congregação'
        }
    ))

    tema = forms.ModelChoiceField(queryset=Temas.objects.all().order_by('tema'), widget=forms.Select(
        attrs={
            'class':'form-control-1'
        }
    ))

    email = forms.EmailField(label='Nome', widget=forms.TextInput(
        attrs={
            'class': 'form-control-1',
            'placeholder': 'Digite o seu email'
        }
    ))
    dia = forms.CharField(label='Nome', widget=forms.TextInput(
        attrs={
            'class': 'form-control-1',
            'placeholder': 'Digite o dia da reunião da congregação'
        }
    ))
 
    data = forms.DateField(
        widget = forms.DateInput(format=('%d-%m-%Y'),
            attrs={
            'class':'form-control-1', 
            'placeholder':'Selecione uma data'})

)

    horario = forms.CharField(label='Nome', widget=forms.TextInput(
        attrs={
            'class': 'form-control-1',
            'placeholder': 'Digite o dia da reunião da congregação'
        }
    ))
    
    horario = forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={
            'class': 'form-control-1',
            'placeholder': 'Digite o horário da reunião'
        }))

    

    ajuda = forms.ChoiceField(label='Carrinho', choices=a_list(), widget=forms.Select(
        attrs={
            'class':'form-control-1'
        }
    ))

    custo = forms.CharField(label='Nome', widget=forms.TextInput(
        attrs={
            'class': 'form-control-1',
            'placeholder': 'Digite o valor do custo'
        }
    ))

#    avaliacao = forms.ChoiceField(label='Carrinho', choices=score(), widget=forms.Select(
#        attrs={
#            'class':'form-control-1'
#        }
#    ))

