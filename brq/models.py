from django.db import models

class Cliente(models.Model):
    TIPO_PESSOA = (
        ('F', 'Física'),
        ('J', 'Jurídica')
    )

    id_cliente = models.CharField(primary_key=True, max_length=14)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=15)
    tipoPessoa = models.CharField(choices=TIPO_PESSOA, max_length=1, blank=False, null=False)

    def __str__(self):
        return self.nome

class TipoTransacao(models.Model):
    DESCRICAO = (
        ('S', 'SAQUE'),
        ('D', 'DEPÓSITO'),
        ('T', 'TRANSFÊRENCIA'),
        ('E', 'EMPRÉSTIMO')
    )
    descricao = models.CharField(max_length=1, choices=DESCRICAO, unique=True)

    def __str__(self):
        return self.descricao

class Transacao(models.Model):

    data = models.DateField()
    valor = models.DecimalField(decimal_places=2, max_digits=5)
    tipoTransacao = models.ForeignKey(
        TipoTransacao,
        on_delete=models.CASCADE
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "Cliente: {}\nTipo de Transação: {}\nValor: {}\nData: {}".format(self.cliente, self.tipoTransacao, self.valor, self.data)
