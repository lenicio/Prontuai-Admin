# Generated by Django 5.2.1 on 2025-05-27 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EspecialidadeMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Ex: Anestesista, Pediatra, Cardiologista...', max_length=200, unique=True, verbose_name='Especialidade Médica')),
                ('criado_em', models.DateTimeField(auto_now_add=True, help_text='Data de criação', verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, help_text='Data de atualização', verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Especialidade Médica',
                'verbose_name_plural': 'Especialidades Médicas',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do paciente', max_length=200, verbose_name='Nome')),
                ('data_nascimento', models.DateField(help_text='Data de nascimento', verbose_name='Data de nascimento')),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outros', 'Outros')], help_text='Sexo do paciente', max_length=10, verbose_name='Sexo')),
                ('cpf', models.CharField(help_text='EX: XXXXXXXXX', max_length=11, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(help_text='RG do paciente', max_length=9, verbose_name='RG')),
                ('nome_mae', models.CharField(help_text='Nome da mae', max_length=200, verbose_name='Nome mae')),
                ('nome_pai', models.CharField(blank=True, help_text='Nome da pai', max_length=200, verbose_name='Nome pai')),
                ('telefone_principal', models.CharField(help_text='Ex:, XXXXXX-XXXX', max_length=11, verbose_name='Telefone')),
                ('telefone_segundario', models.CharField(blank=True, help_text='Ex: XXXXXX-XXXX', max_length=11, null=True, verbose_name='Telefone Segundario')),
                ('email', models.EmailField(blank=True, help_text='Email do paciente', max_length=100, null=True, verbose_name='Email')),
                ('tipo_sanguineo', models.CharField(blank=True, choices=[('A⁺', 'A⁺'), ('A⁻', 'A⁻'), ('B⁺', 'B⁺'), ('B⁻', 'B⁻'), ('AB⁺', 'AB⁺'), ('AB⁻', 'AB⁻'), ('O⁺', 'O⁺'), ('O⁻', 'O⁻')], help_text='Tipo Sanguineo do paciente', null=True, verbose_name='Tipo Sanguineo')),
                ('criado_em', models.DateTimeField(auto_now_add=True, help_text='Data de criação', verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, help_text='Data de atualização', verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do médico', max_length=200, verbose_name='Nome')),
                ('telefone', models.CharField(help_text='Ex: XXXXXX-XXXX', max_length=11, verbose_name='Telefone')),
                ('email', models.EmailField(blank=True, help_text='Email do médico', max_length=100, unique=True, verbose_name='Email')),
                ('data_nascimento', models.DateField(help_text='Data de nascimento', verbose_name='Data de nascimento')),
                ('cpf', models.CharField(help_text='EX: XXXXXXXXX', max_length=11, unique=True, verbose_name='CPF')),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], default='Ativo', help_text='Status do médico', max_length=10, verbose_name='Status')),
                ('crm', models.CharField(help_text='Ex: CRM/UF XXXXXX', max_length=13, unique=True, verbose_name='CRM')),
                ('criado_em', models.DateTimeField(auto_now_add=True, help_text='Data de criação', verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, help_text='Data de atualização', verbose_name='Atualizado em')),
                ('especialidades', models.ManyToManyField(to='prontuario.especialidademedica', verbose_name='Especialidades')),
            ],
            options={
                'verbose_name': 'Médico',
                'verbose_name_plural': 'Médicos',
            },
        ),
    ]
