from django.shortcuts import render
from .m_forms import TesteForm

def teste(request):
    form = TesteForm()
    
    return render(request, 'm_teste.html', {'form': form})

