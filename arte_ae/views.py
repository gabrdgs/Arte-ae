from django.shortcuts import render
from arte_ae.forms import UserModelForm

# Create your views here.
def index(req):
  return render(req, 'index.html')

def login(req):
  return render(req, 'login.html')

def cadastro_usuario(req):
  form = UserModelForm(req.POST or None)

  if form.is_valid():
    form.save()
    context = {
      'msg': 'Cadastrado com sucesso'
    }
    return render(req, 'cadastro-usuario.html', context)
  context = {
    'form': form
  }
  return render(req, 'cadastro-usuario.html', context)