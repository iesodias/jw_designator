from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from jw_designator.grupos.forms import GruposForm
from jw_designator.grupos.models import Grupo
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='my_redirect_field')
def grupo(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def  create(request):
    form = GruposForm(request.POST)
    if form.is_valid():
        Grupo.objects.create(**form.cleaned_data)
        messages.success(request, 'Cadastro Realizado com Sucesso!')
        return HttpResponseRedirect('/grupo/')
    else:
        return render(request, 'grupos/grupo.html', {'form': form})

def new(request):
    return render(request, 'grupos/grupo.html', {'form': GruposForm()})
