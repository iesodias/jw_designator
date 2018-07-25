from django.shortcuts import render
#from django.template.response import TemplateResponse
#from jw_designator.cadastros.models import Cadastro
from jw_designator.indicadores.forms import IndicadoresForm
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='my_redirect_field')
def indicadores(request):
    form = {'form': IndicadoresForm()}
    return render(request, 'indicador/indicadores.html', form)


#def indicadores(request):
#    data = Cadastro.objects.all()
#    return TemplateResponse (request, 'indicador/indicadores.html', {'data': data})

#def indicadores(request):
#    return render(request, 'indicadores.html')
