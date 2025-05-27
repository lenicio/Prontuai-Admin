from django.db import models


class EspecialidadeMedica(models.Model):
    nome = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Especialidade Médica",
        help_text="Ex: Anestesista, Pediatra, Cardiologista...",
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
        verbose_name = "Especialidade Médica"
        verbose_name_plural = "Especialidades Médicas"
