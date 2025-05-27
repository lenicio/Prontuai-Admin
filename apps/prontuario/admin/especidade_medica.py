from django.contrib import admin
from apps.prontuario.models.especialidade_medica import EspecialidadeMedica


@admin.register(EspecialidadeMedica)
class EspecialidadeMedicaAdmin(admin.ModelAdmin):
    list_diplay = ['nome']
    search_fields = ['nome']
    ordering = ['nome']
    readonly_fields = ['criado_em', 'atualizado_em']