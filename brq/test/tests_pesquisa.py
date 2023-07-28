from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from brq.models import Transacao, Cliente, TipoTransacao


class PesquisaTestCase(APITestCase):

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


    def test_pesquisa_com_parametro_data_incompleto(self):
        response = self.client.get('/transacoes/?data_inicio=2023-07-25')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_pesquisa_com_parametro_data_completo(self):
        response = self.client.get('/transacoes/?data_inicio=2023-07-25&data_final=2023-07-27')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_pesquisa_com_parametro_data_completo_e_tipo_pessoa(self):
        response = self.client.get('/transacoes/?data_inicio=2023-07-25&data_final=2023-07-27&tipoPessoa=F')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_pesquisa_com_parametro_data_completo_tipo_pessoa_e_descricao(self):
        response = self.client.get('/transacoes/?data_inicio=2023-07-25&data_final=2023-07-27&tipoPessoa=F&descricao=S')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_pesquisa_com_parametro_data_completo_tipo_pessoa_e_descricao_e_id_cliente(self):
        response = self.client.get('/transacoes/?data_inicio=2023-07-25&data_final=2023-07-27&tipoPessoa=F&descricao=S&idCliente=12345678912')
        self.assertEquals(response.status_code, status.HTTP_200_OK)