from django.contrib import admin
from apps.prontuario.models.medico import Medico



@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'crm', 'telefone', 'email', 'status']
    ordering = ['nome']
    search_fields = ['nome', 'crm', 'cpf', 'telefone']
    list_filter = ['status']
    readonly_fields = ['criado_em', 'atualizado_em']
    filter_horizontal = ['especialidades']