from rest_framework.test import APITestCase
from brq.models import Cliente
from django.urls import reverse
from rest_framework import status


class ClienteTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Clientes-list')
        self.cliente1 = Cliente.objects.create(
            id_cliente="12345678912",
            nome="Teste",
            telefone="(11) 91234-1234",
            tipoPessoa="F"
        )
        self.cliente2 = Cliente.objects.create(
            id_cliente="12345678919",
            nome="Teste dois",
            telefone="(11) 91224-1234",
            tipoPessoa="F"
        )

    def test_requisicao_get_para_listar_cliente(self):
        """Teste para verificar requisicao GET para listar todos os clientes"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_cliente(self):
        """Teste para verificar requisicao POST para criar clientes"""
        data = {
            'id_cliente': '12345678922',
            'nome': 'Testeee',
            'telefone': '(11) 91224-1224',
            'tipoPessoa': 'F'
        }
        response = self.client.post(self.list_url, data=data)
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put_para_atualizar_clientes(self):
        """Teste para verificar requisicao PUT para atualizar dados de clientes"""
        data = {
            'id_cliente': '12345678912',
            'nome': 'Testeee atualizado',
            'telefone': '(11) 91224-1224',
            'tipoPessoa': 'F'
        }
        response = self.client.put('/clientes/12345678912/', data=data)
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_para_deletar_um_cliente(self):
        """Teste para verificar a requisição DELETE"""
        response = self.client.delete('/clientes/12345678912/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
