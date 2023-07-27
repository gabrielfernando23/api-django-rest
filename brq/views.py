from rest_framework import viewsets, status, filters, generics
from rest_framework.response import Response

from brq.filters import TransacaoFilter
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
    filterset_class = TransacaoFilter
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['valor']
    search_fields = ['=valor']

class TransacaoListCreateView(generics.ListCreateAPIView):
    queryset = Transacao.objects.all()
    serializer_class = TransacoesSerializer
    # filterset_class = TransacaoFilter