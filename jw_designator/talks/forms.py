from django import forms

class TalksList(forms.Form):
    Tema = forms.CharField(label='Tema')