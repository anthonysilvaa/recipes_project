from django.contrib import admin
from pessoa.models import PessoaModel

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')

admin.site.register(PessoaModel, PessoaAdmin)