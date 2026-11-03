from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Secretaria, Paciente, Requisicao
from .forms import PacienteForm, RequisicaoUpdateForm
# Create your views here.


def requisicaoLista(request):
    requisicoes = Requisicao.objects.all()
    requisicoes_totais = requisicoes.count() 
    requisicoes_pendentes = requisicoes.filter(status='pendente').count()
    requisicoes_marcadas = requisicoes.filter(status='marcada').count()
    requisicoes_encerradas = requisicoes.filter(status='encerrada').count()
    requisicoes_canceladas = requisicoes.filter(status='cancelada').count()
    
    lista_colunas = ['Recebimento', 'Paciente', 'Procedimento', 'Especificidades', 'Prioridade','Status', 'Ações']
    
    context = {
        'requisicoes': requisicoes,
        'requisicoes_totais': requisicoes_totais,
        'requisicoes_pendentes': requisicoes_pendentes,
        'requisicoes_marcadas': requisicoes_marcadas,
        'requisicoes_encerradas': requisicoes_encerradas,
        'requisicoes_canceladas': requisicoes_canceladas,
        'lista_colunas': lista_colunas,
    }
    return render(request, 'RequisicoesPacientes/requisicoes.html', context)


def requisicaoDetalhes(request, requisicaoId):
    requisicao = Requisicao.objects.get(id=requisicaoId)
    return render(request, 'RequisicoesPacientes/requisicao.html', {'requisicao': requisicao})

def requisicaoEditar(request, requisicaoId):
    requisicao = get_object_or_404(Requisicao, id=requisicaoId)

    if request.method == 'POST':
        form = RequisicaoUpdateForm(request.POST, request.FILES, instance=requisicao)
        if form.is_valid():
            form.save() 
            return redirect('requisicao', requisicaoId=requisicaoId)
    else:
        form = RequisicaoUpdateForm(instance=requisicao)

    return render(request, 'RequisicoesPacientes/editar_requisicao.html', {
        'requisicao': requisicao,
        'form': form,
    })

def requisicaoCriar(request):
    if request.method == 'POST':
        form = RequisicaoUpdateForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()

            return redirect('requisicoes')
    else:
        form = RequisicaoUpdateForm()

    return render(request, 'RequisicoesPacientes/criar_requisicao.html', {
        'form': form,
    })

def requisicaoDeletar(request, requisicaoId):
    requisicao = get_object_or_404(Requisicao, id=requisicaoId)

    if request.method == 'POST':
        requisicao.delete()

        messages.success(request, 'Requisição excluída com sucesso!')

        return redirect('requisicoes')

    return redirect('requisicao', id=requisicaoId)


def pacienteLista(request):
    pacientes = Paciente.objects.all()
    pacientes_totais = pacientes.count() 
    pacientes_requisicoes_pendentes = pacientes.filter(requisicoes__status='pendente').count()
    pacientes_requisicoes_marcadas = pacientes.filter(requisicoes__status='marcada').count()
    lista_colunas = ['Nome', 'Especificidades', 'Cartão SUS','Mais', 'Ações']
    
    context = {
        'pacientes': pacientes,
        'pacientes_totais': pacientes_totais,
        'pacientes_requisicoes_pendentes': pacientes_requisicoes_pendentes,
        'pacientes_requisicoes_marcadas': pacientes_requisicoes_marcadas,
        'lista_colunas': lista_colunas,
    }
    
    return render(request, 'RequisicoesPacientes/pacientes.html', context)


def pacienteDetalhes(request, pacienteId):
    paciente = Paciente.objects.get(id=pacienteId)
    requisicoes = paciente.requisicoes.all()
    requisicoes_totais = requisicoes.count() 
    requisicoes_pendentes = requisicoes.filter(status='pendente').count()
    requisicoes_marcadas = requisicoes.filter(status='marcada').count()
    requisicoes_encerradas = requisicoes.filter(status='encerrada').count()
    requisicoes_canceladas = requisicoes.filter(status='cancelada').count()
    lista_colunas = ['Recebimento', 'Paciente', 'Procedimento', 'Especificidades', 'Prioridade','Status', 'Ações']
    
    context = {
        'paciente': paciente,
        'requisicoes': requisicoes,
        'requisicoes_totais': requisicoes_totais,
        'requisicoes_pendentes': requisicoes_pendentes,
        'requisicoes_marcadas': requisicoes_marcadas,
        'requisicoes_encerradas': requisicoes_encerradas,
        'requisicoes_canceladas': requisicoes_canceladas,
        'lista_colunas': lista_colunas,
    }
    return render(request, 'RequisicoesPacientes/paciente.html', context)


def pacienteCriar(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST, request.FILES)
        
        if form.is_valid():
            paciente = form.save(commit=False)
            from .models import Secretaria
            paciente.secretaria = Secretaria.objects.first() 
            
            
            paciente.save()

            return redirect('pacientes')
    else:
        form = PacienteForm()

    return render(request, 'RequisicoesPacientes/criar_paciente.html', {
        'form': form,
    })


def pacienteEditar(request, pacienteId):
    paciente = get_object_or_404(Paciente, id=pacienteId)

    if request.method == 'POST':
        form = PacienteForm(request.POST, request.FILES, instance=paciente)
        
        if form.is_valid():
            form.save() 

            return redirect('paciente', pacienteId=pacienteId)
    else:
        form = PacienteForm(instance=paciente)

    return render(request, 'RequisicoesPacientes/editar_paciente.html', {
        'paciente': paciente,
        'form': form,
    })


def pacienteEditar(request, pacienteId):
    paciente = get_object_or_404(Paciente, id=pacienteId)

    if request.method == 'POST':
        form = PacienteForm(request.POST, request.FILES, instance=paciente)
        
        if form.is_valid():
            form.save() 

            return redirect('paciente', pacienteId=pacienteId)
    else:
        form = PacienteForm(instance=paciente)

    return render(request, 'RequisicoesPacientes/editar_paciente.html', {
        'paciente': paciente,
        'form': form,
    })
    

def pacienteDeletar(request, pacienteId):
    paciente = get_object_or_404(Paciente, id=pacienteId)

    if request.method == 'POST':
        paciente.delete()

        messages.success(request, 'Paciente excluído com sucesso!')

        return redirect('pacientes')

    return redirect('paciente', id=pacienteId)