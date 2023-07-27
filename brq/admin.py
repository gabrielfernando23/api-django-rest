from django.contrib import admin
from brq.models import Cliente, TipoTransacao, Transacao

class Clientes(admin.ModelAdmin):
    list_display = ('id_cliente', 'nome', 'telefone', 'tipoPessoa')
    list_display_links = ('id_cliente', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Cliente, Clientes)

class TiposDeTransacoes(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao',)
    list_per_page = 10

admin.site.register(TipoTransacao, TiposDeTransacoes)

class Transacoes(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'valor', 'data', 'tipoTransacao')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 10

admin.site.register(Transacao, Transacoes)
