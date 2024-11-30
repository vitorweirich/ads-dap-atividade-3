from django.urls import path
from .views import FuncionarioListAPIView

urlpatterns = [
    path('funcionarios/', FuncionarioListAPIView.as_view(), name='funcionario-list'),
]
