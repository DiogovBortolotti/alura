from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
from django.contrib import auth, messages
from catalogo_receitas.models import Receita


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if not nome.strip():
            messages.error(request, 'Campo não pode ser em branco!')
            return redirect('cadastro')

        email = request.POST.get('email')
        if not email.strip():
            messages.error(request, 'Campo não pode ser em branco!')
            return redirect('cadastro')
        
        senha = request.POST.get('password')
        senha2 = request.POST.get('password2')

        if senha != senha2:
            print('Campos não são iguais')
            messages.error(request, 'Campos não são iguais!')
            return redirect('cadastro')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-MAIL JA CADASTRADO!')

            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'USUÁRIO CADASTRADO COM SUCESSO!')
        return redirect('login')
    
    return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if email == "" or senha =="":
            messages.error(request, 'As senhas não são iguais')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            user_instance = User.objects.get(email=email)
            user = auth.authenticate(request, username=user_instance.username, password=senha)
            if user is not None:
                auth.login(request, user) #A122@gmail.com
                print('Realizou login')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'Realizado o logout com sucesso!')
    return redirect('login')


def dashboard(request):
    if request.user.is_authenticated:
        receitas = Receita.objects.order_by('-data')#.filter(pessoa=request.user.id)
        dados ={'receitas': receitas}


        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')
  
    
def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST.get('nome_receita')
        ingredientes =  request.POST.get('ingredientes')
        modo_preparo = request.POST.get('modo_preparo')
        tempo_preparo = request.POST.get('tempo_preparo')
        rendimento = request.POST.get('rendimento')    
        categoria = request.POST.get('categoria')    
        foto_receita = request.FILES.get('foto_receita')
        receita = Receita.objects.create(#pessoa=user,
        nome_receita=nome_receita,ingredientes=ingredientes, modo_preparo=modo_preparo,tempo_preparo=tempo_preparo,
        rendimento=rendimento, categoria=categoria, #foto_receita=foto_receita
        )
        receita.save() 
        print(nome_receita,ingredientes,modo_preparo,tempo_preparo,rendimento, categoria, foto_receita) 
        return redirect('dashboard')
    return render(request, 'usuarios/cria_receita.html') 