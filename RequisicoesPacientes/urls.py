from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import pacienteDeletar, pacienteEditar, requisicaoLista, requisicaoDetalhes, pacienteLista, pacienteDetalhes, requisicaoDeletar, requisicaoEditar

urlpatterns = [
    path("requisicoes/", requisicaoLista, name="requisicoes"),
    path("requisicoes/<int:requisicaoId>/", requisicaoDetalhes, name="requisicao"),
    path("requisicoes/<int:requisicaoId>/editar/", requisicaoEditar, name="requisicaoEditar"),
    path("requisicao/<int:requisicaoId>/deletar/", requisicaoDeletar, name="requisicaoDeletar"),
    path("pacientes/", pacienteLista, name="pacientes"),
    path("pacientes/<int:pacienteId>/", pacienteDetalhes, name="paciente"),
    path("paciente/<int:pacienteId>/editar/", pacienteEditar, name="pacienteEditar"),
    path("paciente/<int:pacienteId>/deletar/", pacienteDeletar, name="pacienteDeletar"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)