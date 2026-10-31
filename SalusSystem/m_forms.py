# meu_app/forms.py
from django import forms

class TesteForm(forms.Form):
    nome = forms.CharField(
        label="Nome Completo",
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome aqui...'})
    )
    
    data_nascimento = forms.DateField(
        label="Data de Nascimento",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={'placeholder': 'exemplo@email.com'})
    )
    
    estado = forms.ChoiceField(
        label="Estado",
        choices=[('', 'Selecione um estado...'), ('RN', 'Rio Grande do Norte'), ('SP', 'São Paulo'), ('RJ', 'Rio de Janeiro')],
        widget=forms.Select()
    )
    
    observacoes = forms.CharField(
        label="Observações",
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'custom-input', 
            'placeholder': 'Escreva suas observações aqui...',
        })
    )
    
    documento = forms.FileField(
        label="Anexar Documento",
        required=False, # ou True, se for obrigatório
        widget=forms.FileInput(attrs={
            'id': 'file-upload', # Vamos usar esse ID no JS
            'style': 'display: none;' # Esconde o input nativo
        })
    )