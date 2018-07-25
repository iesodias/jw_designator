from django.core import mail
from django.template.loader import render_to_string
from django.shortcuts import render
from jw_designator.discursos.forms import DiscursoForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from jw_designator.discursos.models import Oradores

def discursos(request):
    if request.method == 'POST':
        form = DiscursoForm(request.POST)

        if form.is_valid():
            body = render_to_string('discursos/discurso_email.html', form.cleaned_data)

            mail.send_mail('Confirmação de Inscrição de Orador',
                            body,
                            'contato@jwdesignator.org',
                           ['contato@jwdesignator',form.cleaned_data['email']],
                           html_message=body
                           )
            
            Oradores.objects.create(**form.cleaned_data)
            messages.success(request, 'Solicitação de Orador Realizado com Sucesso!')
            return HttpResponseRedirect('/discursos/')
        else:
            return render(request, 'discursos/discurso.html', {'form':form})

    else:
        context = {'form':DiscursoForm()}
        return render(request, 'discursos/discurso.html', context)

def list_talks(request):
    return render(request,'discursos/list_talk.html')

# Create your views here.