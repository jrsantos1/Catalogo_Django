from django.shortcuts import render
from django.http import HttpResponse
from .models import Moto

# Create your views here.

def index(request):

    motos = Moto.objects.all()


    dados = {
        'motos': motos
    }

    return render(request, 'index.html', dados)

def moto(request, id):
    return render(request, 'receita.html')