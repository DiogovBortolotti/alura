from django.shortcuts import get_object_or_404, render
from .models import Receita
# Create your views here.

def index(request):
    dados = Receita.objects.all()
    return render(request, 'index.html', {'dados_receita': dados})


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    return render(request, 'receita.html', {'receita': receita})