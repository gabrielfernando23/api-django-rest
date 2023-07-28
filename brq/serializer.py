from rest_framework import serializers
from brq.models import Cliente, TipoTransacao, Transacao
from brq.validators import *
from brq.fields import FormattedPhoneNumberField
from decimal import Decimal


class ClientesSerializer(serializers.ModelSerializer):
    transacoes = serializers.SerializerMethodField()
    class Meta:
        model = Cliente
        fields = '__all__'
    def get_transacoes(self, obj):
        transacoes_do_cliente = Transacao.objects.filter(cliente=obj)
        serializer = TransacoesSerializer(transacoes_do_cliente, many=True)
        return serializer.data
    def validate(self, data):
        if not id_eh_valido(data['id_cliente']):
            raise serializers.ValidationError({'id_cliente':'CPF ou CNPJ inválido!'})
        if not nome_eh_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Nome não pode conter números'})
        if not telefone_eh_valido(data['telefone']):
            raise serializers.ValidationError({'telefone':'Telefone inválido'})
        return data


class TiposDeTransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTransacao
        fields = '__all__'

class TransacoesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transacao
        fields = '__all__'

    def validate(self, data):
        if valor_eh_valido(data['valor']):
            raise serializers.ValidationError('Valor não pode ser zero ou negativo!')
        return data