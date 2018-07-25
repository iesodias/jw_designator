from django.contrib import admin
from jw_designator.discursos.models import Oradores

class CadastroModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato', 'tema', 'congregacao', 'data')
    date_hierarchy = ('data')
    search_fields = ('nome', 'tema', 'data')
    list_filter = ('nome', 'data',)

admin.site.register(Oradores, CadastroModelAdmin)

# Register your models here.



