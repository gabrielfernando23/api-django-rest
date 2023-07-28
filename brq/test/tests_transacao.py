from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from brq.models import Transacao, Cliente, TipoTransacao

class TransacaoTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Transacao-list')
        self.cliente1 = Cliente.objects.create(
            id_cliente="12345678912",
            nome="Teste",
            telefone="(11) 91234-1234",
            tipoPessoa="F"
        )
        self.tipo_de_transacao1 = TipoTransacao.objects.create(
            id=1,
            descricao='S'
        )
        self.transacao1 = Transacao.objects.create(
            data='2023-07-27',
            valor='200',
            tipoTransacao_id=1,
            cliente=self.cliente1
        )

    def test_requisicao_get_para_listar_todas_transacoes(self):
        """Teste para listar todas as transações"""
        response = self.client.get('/transacoes/')
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_cadastrar_transacao(self):
        """Teste para verificar requisição post para cadastrar nova transação"""
        data = {
            'data': '2023-07-27',
            'valor': '199.0',
            'tipoTransacao': 1,
            'cliente': '12345678912'
        }
        response = self.client.post(self.list_url, data=data)
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put_para_atualizar_transacao(self):
        data = {
            'data': '2023-07-27',
            'valor': '500.0',
            'tipoTransacao': 1,
            'cliente': '12345678912'
        }
        response = self.client.put('/transacoes/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_delete_para_deletar_uma_transacao(self):
        response = self.client.delete('/transacoes/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)