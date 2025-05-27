from django.db import models
from django.core.exceptions import ValidationError
from .especialidade_medica import EspecialidadeMedica

class Medico(models.Model):

    nome = models.CharField(
        max_length=200,
        verbose_name="Nome",
        help_text="Nome da medico",
    )

    especialidades = models.ManyToManyField(EspecialidadeMedica)

    telefone = models.CharField(
        max_length=11,
        verbose_name="Telefone",
        help_text="Ex: XXXXXX-XXXX",
    )

    email = models.EmailField(
        max_length=100,
        verbose_name="Email",
        help_text="Email da medico",
        unique=True,
        blank=True,
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        help_text="Data de nascimento",
    )

    cpf = models.CharField(
        max_length=11,
        verbose_name="CPF",
        help_text="EX: XXXXXXXXX",
        unique=True,
    )

    status = models.CharField(
        max_length=10,
        choices=[("Ativo", "Ativo"), ("inativo", "inativo")],
        verbose_name="Status",
        help_text="Status do medico",
        default="Ativo",
    )

    crm = models.CharField(
        max_length=13,
        verbose_name="CRM",
        help_text="Ex: CRM/UF XXXXXX",
        unique=True,
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em",
        help_text="Data de criação",
    )

    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em",
        help_text="Data de atualização",
    )

    def clean(self):
        super().clean()

        if len(self.nome) < 3:
            raise ValidationError("O nome precisa ser maior")

        if not self.nome.replace(" ", "").isalpha():
            raise ValidationError("O nome não pode ter numeros")

       

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"
