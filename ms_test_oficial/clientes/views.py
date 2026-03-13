from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Cliente


def lista_clientes(request):
    mostrar_inativos = request.GET.get("mostrar_inativos") == "1"
    if mostrar_inativos:
        clientes = Cliente.objects.all()
    else:
        clientes = Cliente.objects.filter(ativo=True)
    return render(
        request,
        "clientes/lista_clientes.html",
        {"clientes": clientes, "mostrar_inativos": mostrar_inativos},
    )


def _redirect_lista(request):
    url = reverse("lista_clientes")
    if request.POST.get("mostrar_inativos") == "1":
        url += "?mostrar_inativos=1"
    return redirect(url)


def inativar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    cliente.ativo = False
    cliente.save(update_fields=["ativo"])
    return _redirect_lista(request)


def reativar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    cliente.ativo = True
    cliente.save(update_fields=["ativo"])
    return _redirect_lista(request)
