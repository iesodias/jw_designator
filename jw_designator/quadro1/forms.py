from django import forms
from jw_designator.cadastros.models import Cadastro

def periodo():
    BLANK = "---"
    M = 'Manhã'
    T = 'Tarde'
    N = 'Noite'
    periodo = ((BLANK, '---'), (M, 'Manhã'), (T, 'Tarde'), (N, 'Noite'))
    return periodo

class Quadro1Form(forms.Form):

    oracao = forms.ModelChoiceField(label='Grupo', queryset=Cadastro.objects.filter(sexo = 'Masculino', designacao__in=('Ancião','Servo Ministerial', 'Irmão Batizado')).order_by('nome'), widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))

    indicadores = forms.ModelChoiceField(label='Grupo', queryset=Cadastro.objects.filter(sexo = 'Masculino', designacao__in=('Servo Ministerial', 'Irmão Batizado')).order_by('nome'), widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))

    mic_vol = forms.ModelChoiceField(label='Grupo', queryset=Cadastro.objects.filter(sexo = 'Masculino', designacao__in=('Servo Ministerial', 'Irmão Batizado')).order_by('nome'), widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))

    presidente = forms.ModelChoiceField(label='Grupo', queryset=Cadastro.objects.filter(sexo = 'Masculino', designacao__in=('Ancião', 'Servo Ministerial')).order_by('nome'), widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))

    tesouros = forms.ModelChoiceField(label='Grupo', queryset=Cadastro.objects.filter(sexo = 'Masculino', designacao__in=('Ancião', 'Servo Ministerial')).order_by('nome'), widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    )) 

    escola = forms.ModelChoiceField(label='Grupo', queryset=Cadastro.objects.filter(sexo__in=('Masculino','Feminino'), designacao__in=('Ancião', 'Servo Ministerial', 'Irmão Batizado', 'Publicador')).order_by('nome'), widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))

    nv_crista = forms.ModelChoiceField(label='Grupo', queryset=Cadastro.objects.filter(sexo = 'Masculino', designacao__in=('Ancião', 'Servo Ministerial')).order_by('nome'), widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))

    est_biblico = forms.ModelChoiceField(label='Grupo', queryset=Cadastro.objects.filter(sexo = 'Masculino', designacao__in=('Ancião', 'Servo Ministerial')).order_by('nome'), widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))

    leitura = forms.ModelChoiceField(label='Grupo', queryset=Cadastro.objects.filter(sexo = 'Masculino', designacao__in=('Ancião','Servo Ministerial', 'Irmão Batizado')).order_by('nome'), widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    
    carrinho = forms.ModelChoiceField(label='Grupo', queryset=Cadastro.objects.filter(carrinho = 'Sim').order_by('nome'), widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))

    periodo = forms.ChoiceField(label='Grupo', choices=periodo(), widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))

