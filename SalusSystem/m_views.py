from django.shortcuts import render
from django.core.paginator import Paginator
from .m_forms import TesteForm


def teste(request):
    form = TesteForm()
    
    dados_falsos = [f"Item de teste {i}" for i in range(1, 101)]
    
    paginator = Paginator(dados_falsos, 10)
    numero_pagina = request.GET.get('page')
    page_obj = paginator.get_page(numero_pagina)

    contexto = {'form': form, 'page_obj': page_obj}
    
    return render(request, 'm_teste.html', contexto)