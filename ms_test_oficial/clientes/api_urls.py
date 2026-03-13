from django.urls import path
from . import api_views

urlpatterns = [
    path("clientes/", api_views.listar_clientes),
    path("clientes/<int:cliente_id>/inativar/", api_views.inativar_cliente),
    path("clientes/<int:cliente_id>/reativar/", api_views.reativar_cliente),
]
