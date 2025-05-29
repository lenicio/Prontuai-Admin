from django.core.exceptions import ValidationError
from apps.prontuario.utils.sanitiza_nome import sanitiza_nome


def valida_nome(nome):

    nome_sanitizado = sanitiza_nome(nome)

    if not nome_sanitizado.replace(" ", "").isalpha():
        raise ValidationError("O nome não pode ter numeros")
    
    if len(nome_sanitizado.split()) < 2:
        raise ValidationError("É necessario incluir nome e sobrenome")
    
    