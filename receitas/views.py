from django.shortcuts import render, get_list_or_404, get_object_or_404
from receitas.models import ReceitaModel
# Create your views here.


def index(request):

    receitas = ReceitaModel.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': receitas
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




















