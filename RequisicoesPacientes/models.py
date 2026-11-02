from django.db import models
from django.utils import timezone

from .constants import ESPECIFICIDADES_ICONS


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
    secretaria = models.ForeignKey(
        Secretaria, on_delete=models.CASCADE, related_name="pacientes"
    )
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
    comprovanteResidencia = models.FileField(upload_to="comprovantes_residencia/")
    observacoes = models.TextField(blank=True)
    gestante = models.BooleanField(default=False)
    alergias = models.TextField(blank=True)
    oncologico = models.BooleanField(default=False)
    deficiencias = models.JSONField(blank=True, null=True)
    especificidades = models.JSONField(blank=True, null=True)
    end_estado = models.CharField(max_length=50, blank=True, null=True)
    end_municipio = models.CharField(max_length=50, blank=True, null=True)
    end_bairro = models.CharField(max_length=50, blank=True, null=True)
    end_rua = models.CharField(max_length=100, blank=True, null=True)
    end_numero = models.CharField(max_length=10, blank=True, null=True)
    
    @property
    def idade(self):
        hoje = timezone.localdate()
        idade = (
            hoje.year
            - self.dataNascimento.year
            - (
                (hoje.month, hoje.day)
                < (self.dataNascimento.month, self.dataNascimento.day)
            )
        )
        return idade

    @property
    def especificidades_icones(self):
        return [
            ESPECIFICIDADES_ICONS[especificidade]
            for especificidade in (self.especificidades or [])
            if especificidade in ESPECIFICIDADES_ICONS
        ]

    def atualizar_especificidades(self):
        especificidades = self.especificidades or []

        # Especificidades gerenciadas automaticamente
        automaticas = [
            "idoso",
            "menor de idade",
            "criança",
            "bebê",
            "gestante",
            "alergico",
            "oncologico",
            "deficiente",
        ]

        # Preserva apenas as especificidades manuais
        especificidades = [item for item in especificidades if item not in automaticas]

        hoje = timezone.localdate()

        idade = (
            hoje.year
            - self.dataNascimento.year
            - (
                (hoje.month, hoje.day)
                < (self.dataNascimento.month, self.dataNascimento.day)
            )
        )

        # Classificações por idade
        if idade > 60:
            especificidades.append("idoso")

        elif idade < 1:
            especificidades.append("bebê")

        elif idade < 12:
            especificidades.append("criança")

        elif idade < 18:
            especificidades.append("menor de idade")

        # Classificações por condições do paciente
        if self.gestante:
            especificidades.append("gestante")

        if self.alergias:
            especificidades.append("alergico")

        if self.oncologico:
            especificidades.append("oncologico")
        
        if self.deficiencias:
            especificidades.append("pcd")

        # Remove duplicatas
        self.especificidades = list(dict.fromkeys(especificidades))


    def save(self, *args, **kwargs):
        self.atualizar_especificidades()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Requisicao(models.Model):
    CHOICES_PRIORIDADE = {
        "eletiva": "Eletiva",
        "urgencia": "Urgência",
    }
    CHOICES_STATUS = {
        "pendente": "Pendente",
        "marcada": "Marcada",
        "encerrada": "Encerrada",
        "cancelada": "Cancelada",
    }

    paciente = models.ForeignKey(
        Paciente, on_delete=models.CASCADE, related_name="requisicoes"
    )
    cid = models.CharField(max_length=10)
    prioridade = models.CharField(max_length=10, choices=CHOICES_PRIORIDADE)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS)
    procedimento = models.CharField(max_length=100)
    data_expedicao = models.DateField()
    data_recebimento = models.DateField(auto_now_add=True)
    data_marcada = models.DateField(blank=True, null=True)
    profissional_solicitante = models.CharField(max_length=100)
    unidade_solicitante = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True)
    documentos = models.FileField(upload_to="documentos_requisicao/", blank=True, null=True)

    def __str__(self):
        return f"Requisição {self.id} - {self.paciente.nome}"
