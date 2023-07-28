#     # filters.py
# import django_filters
# from .models import Transacao
#
#
# class TransacaoFilter(django_filters.FilterSet):
#     data_inicio = django_filters.DateFilter(field_name='data', lookup_expr='gte', required=True)
#     data_final = django_filters.DateFilter(field_name='data', lookup_expr='lte', required=True)
#     id_cliente = django_filters.CharFilter(field_name='cliente__id')
#     tipoPessoa = django_filters.CharFilter(field_name='cliente__tipoPessoa', method='filter_tipo_pessoa')
#     descricao = django_filters.CharFilter(field_name='tipoTransacao__descricao')
#
#
#     class Meta:
#         model = Transacao
#         fields = []
#
#     def filter_tipo_pessoa(self, queryset, nome, value):
#         return queryset.filter(cliente__tipoPessoa=value)