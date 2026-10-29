from django.shortcuts import render
from .models import Secretaria, Paciente, Requisicao
# Create your views here.


def requisicaoLista(request):
    requisicoes = Requisicao.objects.all()
    requisicoes_totais = requisicoes.count() 
    requisicoes_pendentes = requisicoes.filter(status='pendente').count()
    requisicoes_marcadas = requisicoes.filter(status='marcada').count()
    requisicoes_encerradas = requisicoes.filter(status='encerrada').count()
    requisicoes_canceladas = requisicoes.filter(status='cancelada').count()
    
    context = {
        'requisicoes': requisicoes,
        'requisicoes_totais': requisicoes_totais,
        'requisicoes_pendentes': requisicoes_pendentes,
        'requisicoes_marcadas': requisicoes_marcadas,
        'requisicoes_encerradas': requisicoes_encerradas,
        'requisicoes_canceladas': requisicoes_canceladas,
    }
    return render(request, 'RequisicoesPacientes/requisicoes.html', context)

def requisicao_detalhes(request, requisicaoId):
    requisicao = Requisicao.objects.get(id=requisicaoId)
    return render(request, 'requisicao.html', {'requisicao': requisicao})

def pacienteLista(request):
    pacientes = Paciente.objects.all()
    pacientes_totais = pacientes.count() 
    pacientes_requisicoes_pendentes = pacientes.filter(requisicoes__status='pendente').count()
    pacientes_requisicoes_marcadas = pacientes.filter(requisicoes__status='marcada').count()
    
    context = {
        'pacientes': pacientes,
        'pacientes_totais': pacientes_totais,
        'pacientes_requisicoes_pendentes': pacientes_requisicoes_pendentes,
        'pacientes_requisicoes_marcadas': pacientes_requisicoes_marcadas,
    }
    
    return render(request, 'RequisicoesPacientes/pacientes.html', context)

def paciente_detalhes(request, pacienteId):
    paciente = Paciente.objects.get(id=pacienteId)
    return render(request, 'paciente.html', {'paciente': paciente})

