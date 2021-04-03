from rest_framework import viewsets, filters
from client.serializers import ClientSerializer
from client.models import Client
from django_filters.rest_framework import DjangoFilterBackend


class ClientsViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']
    filterset_fields = ['is_active']
