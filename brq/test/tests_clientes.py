from rest_framework.test import APITestCase
from brq.models import Cliente
from django.urls import reverse
from rest_framework import status

class ClienteTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Clientes-list')
        self.curso_1 = Cliente.objects.create(
            id_cliente="12345678912",
            nome="Teste",
            telefone="(11) 91234-1234",
            tipoPessoa="F"
        )

    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar requisicao GET para listar todos os cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
