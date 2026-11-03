# meu_app/forms.py
from django import forms
from .models import Paciente, Requisicao


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nome', 'racaCor', 'sexo', 'dataNascimento', 'telefone', 
            'nomeMae', 'municipioNascimento', 'cpf', 'rg', 'cartaoSus', 
            'comprovanteResidencia', 'observacoes', 'gestante', 'alergias', 
            'oncologico', 'deficiencias', 'especificidades',
            'end_estado', 'end_municipio', 'end_bairro', 'end_rua', 'end_numero'
        ]
        
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome completo do paciente'}),
            'racaCor': forms.TextInput(attrs={'placeholder': 'Ex: Branca, Parda, Preta...'}),
            'sexo': forms.TextInput(attrs={'placeholder': 'Ex: Masculino, Feminino'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(00) 00000-0000'}),
            'nomeMae': forms.TextInput(attrs={'placeholder': 'Nome completo da mãe'}),
            'municipioNascimento': forms.TextInput(attrs={'placeholder': 'Cidade onde nasceu'}),
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00'}),
            'rg': forms.TextInput(attrs={'placeholder': '00.000.000-0'}),
            'cartaoSus': forms.TextInput(attrs={'placeholder': '000 0000 0000 0000'}),
            
            'dataNascimento': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            
            'comprovanteResidencia': forms.FileInput(attrs={'class': 'custom-file-input'}),
            
            'observacoes': forms.Textarea(attrs={'placeholder': 'Observações gerais...', 'rows': 3}),
            'alergias': forms.Textarea(attrs={'placeholder': 'Descreva as alergias...', 'rows': 2}),
            
            'end_estado': forms.TextInput(attrs={'placeholder': 'Ex: RN'}),
            'end_municipio': forms.TextInput(attrs={'placeholder': 'Ex: Natal'}),
            'end_bairro': forms.TextInput(attrs={'placeholder': 'Ex: Centro'}),
            'end_rua': forms.TextInput(attrs={'placeholder': 'Ex: Rua das Flores'}),
            'end_numero': forms.TextInput(attrs={'placeholder': 'Ex: 123'}),
            
            'gestante': forms.CheckboxInput(),
            'oncologico': forms.CheckboxInput(),
            
            'deficiencias': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Lista de deficiências (JSON)'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.required:
                field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' required-field'

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        cpf_numeros = ''.join(filter(str.isdigit, cpf))
        if len(cpf_numeros) != 11:
            raise forms.ValidationError("O CPF deve conter 11 dígitos numéricos.")
        return cpf
    

class BaseRequisicaoForm(forms.ModelForm):
    class Meta:
        model = Requisicao
        fields = [
            'paciente', 'cid', 'prioridade', 'procedimento', 
            'data_expedicao', 'profissional_solicitante', 
            'unidade_solicitante', 'observacoes', 'documentos'
        ]
        
        widgets = {
            'paciente': forms.Select(attrs={'class': 'custom-select'}),
            'cid': forms.TextInput(attrs={'placeholder': 'Ex: A00.0'}),
            'prioridade': forms.Select(attrs={'class': 'custom-select'}),
            'procedimento': forms.TextInput(attrs={'placeholder': 'Ex: Eletrocardiograma'}),
            'data_expedicao': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'profissional_solicitante': forms.TextInput(attrs={'placeholder': 'Nome do médico/profissional'}),
            'unidade_solicitante': forms.TextInput(attrs={'placeholder': 'Hospital / Clínica'}),
            'observacoes': forms.Textarea(attrs={'placeholder': 'Observações adicionais...', 'rows': 3}),
            'documentos': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['paciente'].queryset = Paciente.objects.all().order_by('nome')


class RequisicaoCreateForm(BaseRequisicaoForm):
    pass

class RequisicaoUpdateForm(BaseRequisicaoForm):
    class Meta(BaseRequisicaoForm.Meta):
        fields = BaseRequisicaoForm.Meta.fields + ['status'] 
        
        widgets = BaseRequisicaoForm.Meta.widgets.copy()
        widgets.update({
            'status': forms.Select(attrs={'class': 'custom-select'}),
        })

    def clean_data_marcada(self):
        data_marcada = self.cleaned_data.get('data_marcada')
        status = self.cleaned_data.get('status')
        
        if status == 'marcada' and not data_marcada:
            raise forms.ValidationError("A data de marcação é obrigatória quando o status é 'Marcada'.")
            
        return data_marcada
