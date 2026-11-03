from django.contrib.admin import forms
from django import forms


class RequisicaoForm(forms.Form):
    nome = forms.CharField(
        label = 'Nome',
        widget = forms.TextInput(attrs={'placeholder': 'Rosâgela Omar Crislândia'})
    )
    sexo = forms.ChoiceField(
        label = 'Sexo',
        widget = forms.Select(choices=[('M', 'Masculino'), ('F', 'Feminino')])
        )
    idade = forms.DateField(
        label = 'Idade',
        widget = forms.DateInput(attrs={'placeholder': 'Idade'})
    )
    deficiencia = forms.ChoiceField(
        label = 'Deficiência',
        widget = forms.Select(choices=[('Sim', 'Sim'), ('Não', 'Não')])
    )
    alergia = forms.ChoiceField(
        label = 'Alergia',
        widget = forms.Select(choices=[('Sim', 'Sim'), ('Não', 'Não')])
    )
    gravidez = forms.ChoiceField(
        label = 'Gravidez',
        widget = forms.Select(choices=[('Sim', 'Sim'), ('Não', 'Não')])
    )
    oncologia = forms.ChoiceField(
        label = 'Oncologia',    
        widget = forms.Select(choices=[('Sim', 'Sim'), ('Não', 'Não')])
    )
    idoso = forms.ChoiceField(
        label = 'Idoso',
        widget = forms.Select(choices=[('Sim', 'Sim'), ('Não', 'Não')])
    )
    observacao = forms.CharField(
        label = 'Observação',   
        widget = forms.Textarea(attrs={'placeholder': 'Observação'})
    )
    cid = forms.CharField(
        label = 'CID',
        widget = forms.TextInput(attrs={'placeholder': 'CID'})
    )
    status = forms.ChoiceField(
        label = 'Status',   
        widget = forms.Select(choices=[('Pendente', 'Pendente'), ('Aprovado', 'Aprovado'), ('Rejeitado', 'Rejeitado')])
    )
    prioridade = forms.ChoiceField(
        label = 'Prioridade',
        widget = forms.Select(choices=[('Baixa', 'Baixa'), ('Média', 'Média'), ('Alta', 'Alta')])
    )
    data_expedicao = forms.DateField(
        label = 'Data de Expedição',
        widget = forms.DateInput(attrs={'placeholder': 'Data de Expedição'})
    )
    data_recebimento = forms.DateField(
        label = 'Data de Recebimento',
        widget = forms.DateInput(attrs={'placeholder': '09/12/2026'})
    )
    marcada_para = forms.DateField(
        label = 'Marcada Para',
        widget = forms.DateInput(attrs={'placeholder': '21/12/2026'})
    )
    profissional_solicitante = forms.CharField(
        label = 'Profissional Solicitante',
        widget = forms.TextInput(attrs={'placeholder': 'Carlos Diogo Cavalgante'})
    )
    cnis = forms.CharField(
        label = 'CNIS',
        widget = forms.TextInput(attrs={'placeholder': 'CNIS'})
    )
    cbo = forms.CharField(
        label = 'CBO',
        widget = forms.TextInput(attrs={'placeholder': '00000'})
    )
    unidade_saude_solicitante = forms.CharField(
        label = 'Unidade de Saúde Solicitante',
        widget = forms.TextInput(attrs={'placeholder': 'Joana Cunha '})
    )
    cnes = forms.CharField(
        label = 'CNES',
        widget = forms.TextInput(attrs={'placeholder': '0000000000'})
    )
    indicacao_clinica = forms.CharField(
        label = 'Indicação Clínica',
        widget = forms.TextInput(attrs={'placeholder': 'Gripe'})
    )
    procedimento = forms.CharField(
        label = 'Procedimento',
        widget = forms.TextInput(attrs={'placeholder': 'Exame'})
    )
    sigtap = forms.CharField(
        label = 'SIGTAP',
        widget = forms.TextInput(attrs={'placeholder': '0000000000'})
    )
    observacao = forms.CharField(
        label = 'Observação',
        widget = forms.Textarea(attrs={'placeholder': 'Escreva aqui a observação'})
    )
    papel_requisicao = forms.CharField(
        label = 'Papel da Requisição',
        widget = forms.FileInput(attrs={'placeholder': 'Requisição'})
    )

class PacienteForm(forms.Form):
        nome = forms.CharField(
            label = 'Nome',
            widget = forms.TextInput(attrs={'placeholder': 'Rosâgela Omar Crislândia'})
        )
        idade = forms.DateField(
            label = 'Idade',    
            widget = forms.DateInput(attrs={'placeholder': '43'})
        )
        racaCor = forms.ChoiceField(
            label = 'Raça/Cor',
            widget = forms.Select(choices=[('Branco', 'Branco'), ('Negro', 'Negro'), ('Pardo', 'Pardo'), ('Amarelo', 'Amarelo'), ('Indígena', 'Indígena')]) 
        )
        nome_Mae = forms.CharField(
            label = 'Nome da Mãe',
            widget = forms.TextInput(attrs={'placeholder': 'Fernanda Omar'})
        )
        municipio_nascimento = forms.CharField(
            label = 'Município de Nascimento',
            widget = forms.TextInput(attrs={'placeholder': 'Pau dos Ferros'})
        )
        data_nascimento = forms.DateField(
            label = 'Data de Nascimento',
            widget = forms.DateInput(attrs={'placeholder': '21/12/2026'})
        )
        email = forms.EmailField(
            label = 'Email',
            widget = forms.EmailInput(attrs={'placeholder': 'email@exemplo.com'})
        )
        celular = forms.CharField(
            label = 'Celular',
            widget = forms.TextInput(attrs={'placeholder': 'Celular'})
        )
        cidade = forms.CharField(
            label = 'Cidade',
            widget = forms.TextInput(attrs={'placeholder': 'Pau dos Ferros'})
        )
        rua = forms.CharField(
            label = 'Rua',
            widget = forms.TextInput(attrs={'placeholder': 'Gira Sol'})
        )
        bairro = forms.CharField(
            label = 'Bairro',
            widget = forms.TextInput(attrs={'placeholder': 'Bairro'})
        )
        numero = forms.CharField(
            label = 'Número',
            widget = forms.TextInput(attrs={'placeholder': '214'})
        )
        deficiencia = forms.ChoiceField(
            label = 'Deficiência',
            widget = forms.Select(choices=[('Sim', 'Sim'), ('Não', 'Não')])
        )
        alergia = forms.ChoiceField(
            label = 'Alergia',
            widget = forms.Select(choices=[('Sim', 'Sim'), ('Não', 'Não')])
        )
        gravidez = forms.ChoiceField(
            label = 'Gravidez',
            widget = forms.Select(choices=[('Sim', 'Sim'), ('Não', 'Não')])
        )
        oncologia = forms.ChoiceField(
            label = 'Oncologia',
            widget = forms.Select(choices=[('Sim', 'Sim'), ('Não', 'Não')])
        )
        idoso = forms.ChoiceField(
            label = 'Idoso',
            widget = forms.Select(choices=[('Sim', 'Sim'), ('Não', 'Não')])
        )
        cpf = forms.CharField(
            label = 'CPF',
            widget = forms.TextInput(attrs={'placeholder': '000.000.000-00'})
        )
        rg = forms.CharField(
            label = 'RG',
            widget = forms.TextInput(attrs={'placeholder': '00.000.000-0'})
        )
        cartao_sus = forms.CharField(
            label = 'Cartão SUS',
            widget = forms.TextInput(attrs={'placeholder': 'Cartão SUS'})
        )
        comprovante_residencia = forms.FileField(
            label = 'Comprovante de Residência',
            widget = forms.FileInput(attrs={'placeholder': 'Comprovante de Residência'})
        )
        observacao = forms.CharField(
            label = 'Observação',
            widget = forms.Textarea(attrs={'placeholder': 'Escreva aqui a observação'})
        )