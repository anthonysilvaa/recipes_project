from django.shortcuts import render, get_list_or_404, get_object_or_404
from receitas.models import ReceitaModel
from django.core.paginator import Page, Paginator, PageNotAnInteger
# Create your views here.


def index(request):

    receitas = ReceitaModel.objects.order_by('-data_receita').filter(publicada=True)
    paginator = Paginator(receitas, 3)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    dados = {
        'receitas': receitas_por_pagina
    }

    return render(request, 'receitas/index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(ReceitaModel, pk=receita_id)

    receita_a_exibir = {
        'receita': receita
    }

    return render(request,'receitas/receita.html', receita_a_exibir)


def buscarView(request):

    lista_receitas = ReceitaModel.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        lista_a_buscar = request.GET['buscar']

        if buscarView:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=lista_a_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'receitas/buscar.html', dados)




















