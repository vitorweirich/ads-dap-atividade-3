from django.urls import path
from .views import FuncionarioListAPIView, ExportFuncionarioCSV

urlpatterns = [
    path('funcionarios/', FuncionarioListAPIView.as_view(), name='funcionario-list'),
    path('funcionarios/export/', ExportFuncionarioCSV.as_view(), name='funcionario-export-csv')
]
