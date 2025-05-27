from django.db import models
from django.core.exceptions import ValidationError


class Paciente(models.Model):

    nome = models.CharField(
        max_length=200,
        verbose_name="Nome",
        help_text="Nome do paciente",
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        help_text="Data de nascimento",
    )

    sexo = models.CharField(
        max_length=10,
        choices=[
            ("Masculino", "Masculino"),
            ("Feminino", "Feminino"),
            ("Outros", "Outros"),
        ],
        verbose_name="Sexo",
        help_text="Sexo do paciente",
    )

    cpf = models.CharField(
        max_length=11,
        verbose_name="CPF",
        help_text="EX: XXXXXXXXX",
        unique=True,
    )

    rg = models.CharField(
        max_length=9,
        verbose_name="RG",
        help_text="RG do paciente"
    )

    nome_mae = models.CharField(
        max_length=200,
        verbose_name="Nome mae",
        help_text="Nome da mae",
    )

    nome_pai = models.CharField(
        max_length=200,
        verbose_name="Nome pai",
        help_text="Nome da pai",
        blank=True,
    )

    telefone_principal = models.CharField(
        max_length=11,
        verbose_name="Telefone",
        help_text="Ex:, XXXXXX-XXXX",
    )

    telefone_segundario = models.CharField(
        max_length=11,
        verbose_name="Telefone Segundario",
        help_text="Ex: XXXXXX-XXXX",
        blank=True,
        null=True
    )

    email = models.EmailField(
        max_length=100,
        verbose_name="Email",
        help_text="Email do paciente",
        blank=True,
        null=True
    )

    tipo_sanguineo = models.CharField(
        choices=[
            ("A⁺", "A⁺"),
            ("A⁻", "A⁻"),
            ("B⁺", "B⁺"),
            ("B⁻", "B⁻"),
            ("AB⁺", "AB⁺"),
            ("AB⁻", "AB⁻"),
            ("O⁺", "O⁺"),
            ("O⁻", "O⁻"),
        ],
        blank=True,
        null=True,
        verbose_name="Tipo Sanguineo",
        help_text="Tipo Sanguineo do paciente",
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


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
