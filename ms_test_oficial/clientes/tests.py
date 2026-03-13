from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from .models import Cliente, TipoCliente


class ClienteViewsTests(TestCase):
    def setUp(self):
        self.cliente_ativo = Cliente.objects.create(
            nome="Ana",
            email="ana@email.com",
            tipo=TipoCliente.PESSOA_FISICA,
            ativo=True,
        )
        self.cliente_inativo = Cliente.objects.create(
            nome="Bruno",
            email="bruno@email.com",
            tipo=TipoCliente.PESSOA_JURIDICA,
            ativo=False,
        )

    def test_listagem_carrega_com_status_200(self):
        response = self.client.get(reverse("lista_clientes"))
        self.assertEqual(response.status_code, 200)

    def test_listagem_exibe_apenas_clientes_ativos_por_padrao(self):
        response = self.client.get(reverse("lista_clientes"))
        self.assertContains(response, "Ana")
        self.assertNotContains(response, "Bruno")

    def test_listagem_exibe_todos_com_filtro(self):
        response = self.client.get(
            reverse("lista_clientes") + "?mostrar_inativos=1"
        )
        self.assertContains(response, "Ana")
        self.assertContains(response, "Bruno")

    def test_inativar_cliente(self):
        response = self.client.post(
            reverse("inativar_cliente", args=[self.cliente_ativo.id]),
            {"mostrar_inativos": "0"},
        )
        self.assertEqual(response.status_code, 302)
        self.cliente_ativo.refresh_from_db()
        self.assertFalse(self.cliente_ativo.ativo)

    def test_reativar_cliente(self):
        response = self.client.post(
            reverse("reativar_cliente", args=[self.cliente_inativo.id]),
            {"mostrar_inativos": "1"},
        )
        self.assertEqual(response.status_code, 302)
        self.cliente_inativo.refresh_from_db()
        self.assertTrue(self.cliente_inativo.ativo)

    def test_reativar_preserva_filtro(self):
        response = self.client.post(
            reverse("reativar_cliente", args=[self.cliente_inativo.id]),
            {"mostrar_inativos": "1"},
        )
        self.assertIn("mostrar_inativos=1", response.url)

    def test_listagem_exibe_tipos_dos_clientes(self):
        response = self.client.get(
            reverse("lista_clientes") + "?mostrar_inativos=1"
        )
        self.assertContains(response, "Pessoa Física")
        self.assertContains(response, "Pessoa Jurídica")


class SeedClientesCommandTests(TestCase):
    def test_seed_cria_clientes_e_eh_idempotente(self):
        call_command("seed_clientes")
        total = Cliente.objects.count()
        self.assertGreaterEqual(total, 10)

        call_command("seed_clientes")
        self.assertEqual(Cliente.objects.count(), total)

    def test_seed_cria_clientes_ativos_e_inativos(self):
        call_command("seed_clientes")
        self.assertTrue(Cliente.objects.filter(ativo=True).exists())
        self.assertTrue(Cliente.objects.filter(ativo=False).exists())
