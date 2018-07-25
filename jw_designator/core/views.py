from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#def home(request):
    #return render(request, 'index.html')

@login_required(redirect_field_name='my_redirect_field')
def home(request):
    return render(request, 'index.html')

