from django.contrib import admin
from jw_designator.grupos.models import Grupo

class GrupoModelAdmin(admin.ModelAdmin):
    list_display = ('grupo', 'nome', 'endereco','sup_grupo' )
    search_fields = ('grupo', 'nome', 'endereco','sup_grupo')
    list_filter = ('grupo', 'nome')

admin.site.register(Grupo, GrupoModelAdmin)
