from django.core.management.base import BaseCommand

from clientes.models import Cliente, TipoCliente

CLIENTES_INICIAIS = [
    {"nome": "Ana", "email": "ana@email.com", "tipo": TipoCliente.PESSOA_FISICA, "ativo": True},
    {"nome": "Bruno", "email": "bruno@email.com", "tipo": TipoCliente.PESSOA_FISICA, "ativo": True},
    {"nome": "Carlos", "email": "carlos@email.com", "tipo": TipoCliente.PESSOA_JURIDICA, "ativo": True},
    {"nome": "Daniela", "email": "daniela@email.com", "tipo": TipoCliente.PESSOA_FISICA, "ativo": True},
    {"nome": "Eduardo", "email": "eduardo@email.com", "tipo": TipoCliente.PESSOA_JURIDICA, "ativo": False},
    {"nome": "Fernanda", "email": "fernanda@email.com", "tipo": TipoCliente.PESSOA_FISICA, "ativo": True},
    {"nome": "Gustavo", "email": "gustavo@email.com", "tipo": TipoCliente.PESSOA_JURIDICA, "ativo": False},
    {"nome": "Helena", "email": "helena@email.com", "tipo": TipoCliente.VIP, "ativo": True},
    {"nome": "Igor", "email": "igor@email.com", "tipo": TipoCliente.PESSOA_FISICA, "ativo": True},
    {"nome": "Juliana", "email": "juliana@email.com", "tipo": TipoCliente.VIP, "ativo": True},
    {"nome": "Lucas", "email": "lucas@email.com", "tipo": TipoCliente.PESSOA_FISICA, "ativo": True},
    {"nome": "Mariana", "email": "mariana@email.com", "tipo": TipoCliente.PESSOA_JURIDICA, "ativo": False},
    {"nome": "Nelson", "email": "nelson@email.com", "tipo": TipoCliente.PESSOA_FISICA, "ativo": True},
    {"nome": "Olivia", "email": "olivia@email.com", "tipo": TipoCliente.VIP, "ativo": True},
    {"nome": "Pedro", "email": "pedro@email.com", "tipo": TipoCliente.PESSOA_JURIDICA, "ativo": True},
    {"nome": "Quintino", "email": "quintino@email.com", "tipo": TipoCliente.PESSOA_FISICA, "ativo": False},
    {"nome": "Renata", "email": "renata@email.com", "tipo": TipoCliente.PESSOA_FISICA, "ativo": True},
    {"nome": "Sofia", "email": "sofia@email.com", "tipo": TipoCliente.VIP, "ativo": True},
    {"nome": "Thiago", "email": "thiago@email.com", "tipo": TipoCliente.PESSOA_JURIDICA, "ativo": True},
    {"nome": "Ursula", "email": "ursula@email.com", "tipo": TipoCliente.PESSOA_FISICA, "ativo": False},
]


class Command(BaseCommand):
    help = "Cria clientes iniciais para ambiente de desenvolvimento."

    def handle(self, *args, **options):
        created_count = 0
        updated_count = 0

        for item in CLIENTES_INICIAIS:
            cliente, created = Cliente.objects.get_or_create(
                email=item["email"],
                defaults={
                    "nome": item["nome"],
                    "tipo": item["tipo"],
                    "ativo": item["ativo"],
                },
            )

            if created:
                created_count += 1
                continue

            fields_to_update = []
            for field in ("nome", "tipo", "ativo"):
                if getattr(cliente, field) != item[field]:
                    setattr(cliente, field, item[field])
                    fields_to_update.append(field)

            if fields_to_update:
                cliente.save(update_fields=fields_to_update)
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seed finalizado. Criados: {created_count} | Atualizados: {updated_count}"
            )
        )
