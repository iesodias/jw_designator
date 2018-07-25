from django.contrib import admin
from jw_designator.cadastros.models import Cadastro

class CadastroModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone', 'sexo', 'designacao', 'carrinho', 'created_at' )
    date_hierarchy = 'created_at'
    search_fields = ('nome', 'endereco', 'carrinho','designacao', 'created_at')
    list_filter = ('endereco', 'designacao')

admin.site.register(Cadastro, CadastroModelAdmin)
