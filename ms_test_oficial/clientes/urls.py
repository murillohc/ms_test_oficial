from django.urls import path

from .views import inativar_cliente, lista_clientes, reativar_cliente

urlpatterns = [
    path("", lista_clientes, name="lista_clientes"),
    path("<int:cliente_id>/inativar/", inativar_cliente, name="inativar_cliente"),
    path("<int:cliente_id>/reativar/", reativar_cliente, name="reativar_cliente"),
]
