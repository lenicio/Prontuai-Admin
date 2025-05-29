from django.contrib import admin
from apps.prontuario.models.paciente import Paciente


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sexo', 'tipo_sanguineo', 'data_nascimento', 'cpf', 'rg','telefone_principal' , 'telefone_segundario', 'email', 'nome_mae', 'nome_pai']
    ordering = ['nome']
    search_fields = ['nome', 'cpf', 'telefone_principal','telefone_segundario', 'nome_mae','nome_pai']
    list_filter = ['tipo_sanguineo', 'sexo']
    readonly_fields = ['criado_em', 'atualizado_em']
    fieldsets = (
        ('Paciente', {
            'fields': ('nome', 'data_nascimento', 'sexo', 'cpf', 'rg', 'nome_mae', 'nome_pai', 'telefone_principal', 'telefone_segundario', 'email', 'tipo_sanguineo')
        }),
        ('Datas', {
            'fields': ('criado_em', 'atualizado_em'), 'classes': ('collapse',)
        }),
    )
