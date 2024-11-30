from django.urls import path
from .views import FuncionarioListAPIView, ExportFuncionarioCSV
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Funcionarios API",
        default_version='v1',
        description="Documentação interativa da API de funcionarios",
        contact=openapi.Contact(email="weirichvitor@gmail.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
)

urlpatterns = [
    path('funcionarios/', FuncionarioListAPIView.as_view(), name='funcionario-list'),
    path('funcionarios/export/', ExportFuncionarioCSV.as_view(), name='funcionario-export-csv'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='api-docs'),
]
