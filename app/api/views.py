import csv
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django.http import HttpResponse
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

class ExportFuncionarioCSV(APIView):
    def get(self, request, *args, **kwargs):
        # Cria uma resposta com tipo de conteúdo CSV
        resonse_file_name = request.GET.get('file_name', 'funcionarios.csv')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{resonse_file_name}"'
        
        # Cria o escritor CSV
        writer = csv.writer(response)
        
        # Cabeçalho do CSV
        writer.writerow(['ID', 'Nome', 'Data de Nascimento', 'Email', 'Profissão'])
        
        # Dados dos funcionários
        funcionarios = Funcionario.objects.all()
        
        for funcionario in funcionarios:
            writer.writerow([
                funcionario.id,
                funcionario.nome,
                funcionario.data_nascimento,
                funcionario.email,
                funcionario.profissao,
            ])
        
        return response
