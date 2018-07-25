from django.shortcuts import render
from jw_designator.quadro1.forms import Quadro1Form
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='my_redirect_field')
def quadro1(request):
    form = {'form': Quadro1Form()}
    return render(request, 'quadro1/quadro.html', form)

@login_required(redirect_field_name='my_redirect_field')
def quadro2(request):
    form = {'form': Quadro1Form()}
    return render(request, 'quadro1/quadros1.html', form)

@login_required(redirect_field_name='my_redirect_field')
def quadro3(request):
    form = {'form': Quadro1Form()}
    return render(request, 'quadro1/quadros2.html', form)

@login_required(redirect_field_name='my_redirect_field')
def carrinho(request):
    form = {'form': Quadro1Form()}
    return render(request, 'quadro1/carrinho.html', form)