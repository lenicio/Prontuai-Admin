import datetime
from django.core.exceptions import ValidationError

def valida_data_nascimento(data_nascimento, modelo=None):
    idade = datetime.date.today() - data_nascimento
    if modelo == 'Médico':
        if data_nascimento > datetime.date.today():
            raise ValidationError("A data de nascimento não pode ser maior que a data atual")
    elif modelo == 'Paciente':
        if data_nascimento > datetime.date.today():
            raise ValidationError("A data de nascimento não pode ser maior que a data atual")
    else:
        raise ValidationError("Modelo não encontrado")