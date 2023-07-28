import re
from rest_framework import serializers

def id_eh_valido(id):
    return len(id) == 11 or len(id) == 14

def nome_eh_valido(nome):
    nome = nome.replace(" ","")
    return nome.isalpha()
def telefone_eh_valido(telefone):
    padrao = r"\(\d{2}\)\s*\d{5}-\d{4}"
    resposta = re.findall(padrao, telefone)
    return resposta

def valor_eh_valido(valor):
    print(valor)
    return valor <= 0