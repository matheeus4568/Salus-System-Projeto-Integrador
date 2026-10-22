from django.shortcuts import render
from .models import Secretaria, Paciente, Requisicao
# Create your views here.


def requisicaoLista(request):
    requisicoes = Requisicao.objects.all()
    return render(request, 'requisicaoLista.html', {'requisicoes': requisicoes})

def requisicao_detalhes(request, requisicaoId):
    requisicao = Requisicao.objects.get(id=requisicaoId)
    return render(request, 'requisicaoDetalhes.html', {'requisicao': requisicao})

def paciente_lista(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacienteLista.html', {'pacientes': pacientes})

def paciente_detalhes(request, pacienteId):
    paciente = Paciente.objects.get(id=pacienteId)
    return render(request, 'pacienteDetalhes.html', {'paciente': paciente})

