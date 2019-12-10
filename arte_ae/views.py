from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from arte_ae.forms import EventoForm

# Create your views here.
@login_required
def painel_de_controle(request):
  form = EventoForm(request.POST or None)
  if form.is_valid():
    form.save()
    context = {
      'msg': 'Evento cadastrado com sucesso'
    }
    return render(request, 'painel-de-controle.html', context)
  context = {
    'form': form
  }
  return render(request, 'painel-de-controle.html', context)

def index(request):
  return render(request, 'index.html')

def do_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('/painel')
    
  return render(request, 'login.html')

def do_logout(request):
  logout(request)
  return redirect('/login')

def cadastro_usuario(request):
  form = UserCreationForm(request.POST)
  if form.is_valid():
    form.save()
    context = {
      'msg': 'Cadastrado com sucesso'
    }
    return render(request, 'cadastro-usuario.html', context)
  context = {
    'form': form
  }
  return render(request, 'cadastro-usuario.html', context)