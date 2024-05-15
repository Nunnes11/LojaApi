from django.http import JsonResponse
from rest_framework import viewsets
from .models import Cliente, Produto
from .serializer import ClienteSerializer, ProdutoSerializer


def clientes(request):
    if request.method == 'GET':
        cliente = {'id':1, 'nome':'Robério'}
        return JsonResponse(cliente)


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


