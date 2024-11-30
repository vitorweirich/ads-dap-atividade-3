import csv
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django.http import HttpResponse
from ..models import Funcionario
from .serializers import FuncionarioSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class FuncionarioPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class FuncionarioListAPIView(generics.ListAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

    pagination_class = FuncionarioPagination


class ExportFuncionarioCSV(APIView):
    @swagger_auto_schema(
        operation_description=(
            "Exporta os funcionários para um arquivo CSV. O arquivo contém as seguintes colunas:\n\n"
            "- **Nome**: Nome do funcionário.\n"
            "- **Data de Nascimento**: Data de nascimento no formato YYYY-MM-DD.\n"
            "- **Email**: Endereço de email.\n"
            "- **Profissão**: Profissão do funcionário.\n\n"
            "### Exemplo de conteúdo do CSV:\n"
            "```\n"
            "Nome,Data de Nascimento,Email,Profissão\n"
            "Maria Silva,1990-01-01,maria@email.com,Engenheira\n"
            "João Souza,1985-05-15,joao@email.com,Professor\n"
            "```"
        ),
        manual_parameters=[
            openapi.Parameter('file_name', openapi.IN_QUERY, description="Nome do arquivo CSV", type=openapi.TYPE_STRING, default='funcionarios.csv')
        ],
        responses={
            200: openapi.Response(description="Arquivo CSV gerado com sucesso.")
        }
    )
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
