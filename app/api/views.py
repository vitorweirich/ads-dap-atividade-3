from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from ..models import Funcionario
from .serializers import FuncionarioSerializer

class FuncionarioPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class FuncionarioListAPIView(generics.ListAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

    pagination_class = FuncionarioPagination
