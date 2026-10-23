from django.contrib import admin
from .models import Secretaria, Paciente, Requisicao

# Register your models here.

@admin.register(Secretaria)
class admin_secretaria(admin.ModelAdmin):
    model = Secretaria
    list_display = ('id', 'nome_secretaria',  'telefone')
    search_fields = ('nome_secretaria', 'codigo_ibge', 'telefone', 'end_estado', 'end_municipio',)
    
@admin.register(Paciente)
class admin_paciente(admin.ModelAdmin):
    model = Paciente
    list_display = ('id', 'nome', 'cpf', 'cartaoSus', 'telefone')
    list_filter = ('gestante', 'racaCor', 'sexo')
    
@admin.register(Requisicao)
class admin_requisicao(admin.ModelAdmin):
    model = Requisicao
    list_display = ('id', 'paciente', 'cid', 'prioridade', 'status', 'procedimento', 'data_expedicao', 'data_recebimento')
    search_fields = ('paciente__nome', 'cid', 'procedimento', 'profissional_solicitante', 'unidade_solicitante')
    verbose_name_plural = "Requisições"
    verbose_name = "Requisição"
    search_help_text = "Pesquisar por paciente, CID, procedimento, profissional solicitante ou unidade solicitante"
    list_filter = ('prioridade', 'status', 'data_expedicao', 'data_recebimento')    