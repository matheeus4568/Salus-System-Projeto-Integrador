from django.urls import path
from .views import pacienteDeletar, requisicaoLista, requisicaoDetalhes, pacienteLista, pacienteDetalhes, requisicaoDeletar

urlpatterns = [
    path("requisicoes/", requisicaoLista, name="requisicoes"),
    path("requisicoes/<int:requisicaoId>/", requisicaoDetalhes, name="requisicao"),
    path("requisicao/<int:requisicaoId>/deletar/", requisicaoDeletar, name="requisicaoDeletar"),
    path("pacientes/", pacienteLista, name="pacientes"),
    path("pacientes/<int:pacienteId>/", pacienteDetalhes, name="paciente"),
    path("paciente/<int:pacienteId>/deletar/", pacienteDeletar, name="pacienteDeletar"),
]
