from rest_framework.test import APITestCase
from rest_framework import status
from brq.models import TipoTransacao
from django.urls import reverse

class TipoTransacaoTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Tipos_De_Transacao-list')
        self.tipo_de_transacao1 = TipoTransacao.objects.create(
            id=1,
            descricao='S'
        )
        self.tipo_de_transacao2 = TipoTransacao.objects.create(
            id=2,
            descricao='D'
        )


    def test_requisicao_para_listar_todos_os_tipos_de_transacao(self):
        """Teste para verificar a requisição GET do modelo tipo transação"""
        response = self.client.get(self.list_url)
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_cadastrar_novo_tipo_de_transacao(self):
        """Teste para verificar a requisição POST para cadastrar um novo tipo de transação"""
        data = {
            'descricao': 'T'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put_para_atualzar_tipo_de_transacao(self):
        """Teste para verificar a requisição PUT para cadastrar um novo tipo de transação"""
        data = {
            'descricao': 'T'
        }
        response = self.client.put('/tipos-de-transacao/1/', data=data)
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_delete_para_deletar_tipo_de_transacao(self):
        """Teste para verificar a requisição DELETE para deletar um tipo de transação"""
        response = self.client.delete('/tipos-de-transacao/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_post_para_tentar_criar_um_tipo_de_transcao_duplicado(self):
        data = {
            'descricao': 'D'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)