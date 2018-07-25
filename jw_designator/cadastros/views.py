from django.shortcuts import render
from jw_designator.cadastros.forms import CadastroForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from jw_designator.cadastros.forms import CadastroForm
from jw_designator.cadastros.models import Cadastro
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='my_redirect_field')
def cadastro(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
    form = CadastroForm(request.POST)
    if form.is_valid():
        #Sucesso no cadastro
        Cadastro.objects.create(**form.cleaned_data)
        messages.success(request, 'Cadastro Realizado com Sucesso!')
        return HttpResponseRedirect('/cadastro/')
    else:
        return render(request, 'cadastros/cadastro.html', {'form': form})

def new(request):
    return render(request, 'cadastros/cadastro.html', {'form': CadastroForm()})