from rest_framework import viewsets, status, filters, generics
from rest_framework.response import Response
from rest_framework import serializers

# from brq.filters import TransacaoFilter
from brq.models import Cliente, TipoTransacao, Transacao
from brq.serializer import ClientesSerializer, TiposDeTransacaoSerializer, TransacoesSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

class TiposDeTransacaoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os tipos de transação"""
    queryset = TipoTransacao.objects.all()
    serializer_class = TiposDeTransacaoSerializer

    def destroy(self, request, *args, **kwargs):
        tipo_transacao = self.get_object()
        print(request)
        transacoes_associadas = Transacao.objects.filter(tipoTransacao=tipo_transacao)

        if transacoes_associadas:
            return Response(
                {"error": "Não é possível excluir o tipo de transação, pois há transações associadas a ele."},
                status=status.HTTP_400_BAD_REQUEST
            )

        tipo_transacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TransacoesViewSet(viewsets.ModelViewSet):
    """Exibindo todas as transações"""
    queryset = Transacao.objects.all()
    serializer_class = TransacoesSerializer

    def get_queryset(self):
        queryset = Transacao.objects.all()

        data_inicio = self.request.query_params.get('data_inicio', None)
        data_final = self.request.query_params.get('data_final', None)
        id_cliente = self.request.query_params.get('id_cliente', None)
        tipo_pessoa = self.request.query_params.get('tipoPessoa', None)
        descricao = self.request.query_params.get('descricao', None)

        if not any([data_inicio, data_final, id_cliente, tipo_pessoa, descricao]):
            return queryset

        if not data_inicio or not data_final:
            return None

        if data_inicio:
            queryset = queryset.filter(data__gte=data_inicio)
        if data_final:
            queryset = queryset.filter(data__lte=data_final)
        if id_cliente:
            queryset = queryset.filter(cliente__id=id_cliente)
        if tipo_pessoa:
            queryset = queryset.filter(cliente__tipoPessoa=tipo_pessoa)
        if descricao:
            queryset = queryset.filter(tipoTransacao__descricao=descricao)

        return queryset

