from django.urls import path
from .views import requisicaoLista, requisicao_detalhes, pacienteLista, paciente_detalhes


urlpatterns = [
    path('requisicoes/', requisicaoLista, name='requisicoes'),
    path('requisicoes/<int:requisicaoId>/', requisicao_detalhes, name='requisicao'),
    path('pacientes/', pacienteLista, name='pacientes'),
    path('pacientes/<int:pacienteId>/', paciente_detalhes, name='paciente')
]
