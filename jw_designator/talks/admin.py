from django.contrib import admin
from jw_designator.talks.models import Temas

class CadastroModelAdmin(admin.ModelAdmin):
    list_display = ('tema',)
    list_filter = ('tema',)
    search_fields = ('tema',)


admin.site.register(Temas, CadastroModelAdmin)

# Register your models here.
