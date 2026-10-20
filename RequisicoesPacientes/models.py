from django.db import models

# Create your models here.
class Secretaria(models.Model):
    nome_secretaria = models.CharField(max_length=100)
    codigo_ibge = models.CharField(max_length=10, unique=True)
    telefone = models.CharField(max_length=20)
    end_estado = models.CharField(max_length=50)
    end_municipio = models.CharField(max_length=50)
    end_bairro = models.CharField(max_length=50)
    end_rua = models.CharField(max_length=100)
    end_numero = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nome_secretaria

class Paciente(models.Model):
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE, related_name='pacientes')
    nome = models.CharField(max_length=100)
    racaCor = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    dataNascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    nomeMae = models.CharField(max_length=100)
    municipioNascimento = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=12)
    cartaoSus = models.CharField(max_length=20, unique=True)
    comprovanteResidencia = models.FileField(upload_to='comprovantes_residencia/')
    observacoes = models.TextField(blank=True)
    gestante = models.BooleanField(default=False)
    alergias = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome
    
class Requisicao(models.Model):
    CHOICES_PRIORIDADE = {
        'eletiva': 'Eletiva',
        'urgencia': 'Urgência',
    }
    CHOICES_STATUS = {
        'pendente': 'Pendente',
        'marcada': 'Marcada',
        'encerrada': 'Encerrada',
        'cancelada': 'Cancelada',
    }
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='requisicoes')
    cid = models.CharField(max_length=10)
    prioridade = models.CharField(max_length=10, choices=CHOICES_PRIORIDADE)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS)
    procedimento = models.CharField(max_length=100)
    data_expedicao = models.DateField()
    data_recebimento = models.DateField(auto_now_add=True)
    profissional_solicitante = models.CharField(max_length=100)
    unidade_solicitante = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True)
    
    def __str__(self):
        return f"Requisição {self.id} - {self.paciente.nome}"