from django.contrib import admin
from receitas.models import ReceitaModel
# Register your models here.

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'pessoa', 'publicada')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 3

admin.site.register(ReceitaModel, ReceitaAdmin)