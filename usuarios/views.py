from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import ReceitaModel

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')
        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request,'Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('Usuário cadastrado com sucesso')
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2
        


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if email == "" or senha == "":
            print('Usuário ou senha vazia não é permitido')
            messages.error(request,'Usuário já cadastrado')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                print('Acesso permitido')
                messages.success(request, 'Acesso realizado com sucesso!')
                return redirect('dashboard')


    return render(request, 'usuarios/login.html')


def dashboard(request):
    if request.user.is_authenticated:

        id = request.user.id
        receitas = ReceitaModel.objects.order_by('-data_receita').filter(pessoa=id)

        dados = {
            'receitas' : receitas
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'usuarios/login.html')

def criar_receitas(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        imagem_receita = request.FILES['imagem_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receita = ReceitaModel.objects.create(pessoa=user,nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo,tempo_preparo=tempo_preparo, rendimento=rendimento,categoria=categoria, imagem_receita=imagem_receita)
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/criar_receitas.html')


def deletar_receita(request, receita_id):
    receita_deletada = ReceitaModel.objects.get(pk=receita_id)
    receita_deletada.delete()

    return render(request, 'usuarios/dashboard.html')

def editar_receita(request, receita_id):
    receita = get_object_or_404(ReceitaModel, pk=receita_id)
    dados = {'receita': receita}

    return render(request, 'usuarios/editar_receita.html', dados)

def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']

        r = ReceitaModel.objects.get(pk=receita_id)

        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']

        if 'imagem_receita' in request.FILES:
            r.imagem_receita = request.FILES['imagem_receita']

        r.save()
        messages.success(request, 'Receita atualizada com sucesso!')
        return redirect('dashboard')



    return render(request, 'usuarios/editar_receita.html')