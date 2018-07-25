from django import forms

def c_grupos():
    BLANK = "---"
    grupo1 = 'Grupo 1'
    grupo2 = 'Grupo 2'
    grupo3 = 'Grupo 3'
    grupo4 = 'Grupo 4'
    grupo5 = 'Grupo 5'
    grupos_lista = ((BLANK, '---'), (grupo1, 'Grupo1'), (grupo2, 'Grupo2'), (grupo3, 'Grupo3'), (grupo3, 'Grupo3'), (grupo4, 'Grupo4'), (grupo5, 'Grupo5'))
    return grupos_lista

class GruposForm(forms.Form):
    grupo = forms.ChoiceField(label='Grupo', choices=c_grupos(), widget=forms.Select(
        attrs={
            'class':'form-control-1'
        }
    ))
    nome = forms.CharField(label='Nome do Grupo', widget=forms.TextInput(
        attrs={
            'class': 'form-control-1',
            'placeholder': 'Digite o nome do grupo aqui...'
        }
    ))
    endereco = forms.CharField(label='Endereço', widget=forms.TextInput(
        attrs={
            'class': 'form-control-1',
            'placeholder': 'Digite o endereço do grupo aqui...'
        }
    ))
    sup_grupo = forms.CharField(label='Superintendente de Grupo', widget=forms.TextInput(
        attrs={
            'class': 'form-control-1',
            'placeholder': 'Digite o nome do Sup de Grupo aqui...'
        }
    ))