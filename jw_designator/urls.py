"""jw_designator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from jw_designator.core import views as jw_designator_views
from jw_designator.cadastros.views import cadastro
from jw_designator.grupos.views import grupo
from jw_designator.indicadores.views import indicadores
from jw_designator.quadro1.views import quadro1, quadro2, quadro3, carrinho
from jw_designator.discursos.views import discursos
from jw_designator.discursos.views import list_talks


urlpatterns = [
    url(r'^', include('jw_designator.accounts.urls')),
    url(r'^$', jw_designator_views.home),
    url(r'^cadastro/$', cadastro),
    url(r'^grupo/$', grupo),
    url(r'^indicadores/$', indicadores),
    url(r'^quadro1/$', quadro1),
    url(r'^quadro2/$', quadro2),
    url(r'^quadro3/$', quadro3),
    url(r'^discursos/$', discursos),
    url(r'^carrinho/$', carrinho),
    url(r'^talks/$', list_talks),
    url(r'^admin/', admin.site.urls),
]