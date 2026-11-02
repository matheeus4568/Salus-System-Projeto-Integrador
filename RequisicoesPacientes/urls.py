from django.urls import path
from .views import requisicaoLista, requisicaoDetalhes, pacienteLista, pacienteDetalhes


urlpatterns = [
    path('requisicoes/', requisicaoLista, name='requisicoes'),
    path('requisicoes/<int:requisicaoId>/', requisicaoDetalhes, name='requisicao'),
    path('pacientes/', pacienteLista, name='pacientes'),
    path('pacientes/<int:pacienteId>/', pacienteDetalhes, name='paciente')
]
