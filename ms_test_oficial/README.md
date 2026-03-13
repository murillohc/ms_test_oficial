# Teste Prático — Desenvolvedor(a) Júnior Python/Django

## 1. Objetivo do teste

Este teste tem como objetivo avaliar sua capacidade de realizar uma pequena evolução em um projeto Django já existente, de forma funcional, organizada e coerente.

No dia a dia do MB, grande parte do trabalho envolve:
- entender requisitos simples de negócio
- alterar código existente
- ajustar models, views, templates e queries
- implementar mudanças com cuidado
- validar o comportamento da funcionalidade
- explicar com clareza o que foi feito

Este teste foi pensado para simular esse tipo de cenário de forma objetiva e justa.

---

## 2. Contexto

Você recebeu um projeto Django base já funcional com um módulo de clientes.

Atualmente:
- existe um model `Cliente`
- existe uma listagem de clientes
- os clientes cadastrados aparecem normalmente na tela

Precisamos evoluir esse projeto para permitir a **inativação e reativação de clientes**, além de ajustar a listagem para respeitar essa regra.

---

## 3. Desafio

Implementar a funcionalidade de **inativação de clientes**, fazendo com que clientes inativos não apareçam na listagem padrão.

---

## 4. Requisitos obrigatórios

### 4.1. Alteração no model
1. Adicionar ao model `Cliente` o campo `ativo`
2. Exibir apenas clientes ativos por padrão
3. Permitir visualizar todos os clientes com filtro opcional
4. Criar forma de inativar e reativar clientes
5. Criar pelo menos 2 testes automatizados
6. Atualizar o `seed_clientes` para gerar uma massa de dados
7. Separe o backend do frontend, para boas práticas de desenvolvimento:
- O frontend será feito em um novo projeto que irá acessar as informações deste projeto;
- O frontend deve ser feito em Angular e consumir endpoints do backend;
- Pode utilizar no backend o DRF (Django Rest Framework) para criação dos endpoints;
8. A melhor solução para este teste não é a mais complexa e sim:
- a mais simples;
- a mais clara;
- a mais funcional;
- a mais organizada;
9. Ao final, atualize este README com uma seção chamada "O que foi implementado", descrevendo brevemente:
- o que você fez;
- eventuais decisões tomadas;
- qualquer observação importante sobre sua implementação;
- como rodar o projeto completo, dividido em backend e frontend.
10. Você pode utilizar IA como apoio no desenvolvimento, porém esperamos que você:
- entenda o que implementou
- consiga explicar suas escolhas
- consiga responder perguntas simples sobre o próprio código
11. Junto com a entrega faça um vídeo de no máximo 10 minutos explicando o que foi feito, junto com as envidências do software rodando.

---

## 5. Bônus inicial:

```python
## Como rodar o projeto
```bash
python -m venv .venv
source .venv/bin/activate
pip install django
python manage.py migrate
python manage.py runserver
```

---

## 6. O que foi implementado

### Alterações realizadas

1. **Campo `ativo` no model Cliente** — adicionado como `BooleanField(default=True)`. Todos os clientes são ativos por padrão ao serem criados.

2. **Listagem com filtro** — a listagem exibe apenas clientes ativos por padrão. Para ver todos (incluindo inativos), basta acessar com o parâmetro `?todos=1`.

3. **Inativar e reativar** — criadas views e endpoints que permitem alterar o status do cliente via POST (template) ou PATCH (API).

4. **Testes automatizados** — 8 testes cobrindo: listagem (ativos, todos, tipos), inativação, reativação, seed (criação e idempotência).

5. **Seed atualizado** — expandido de 10 para 20 clientes, incluindo clientes com `ativo=False` para ter uma massa de dados mais realista.

6. **API REST com DRF** — criada API completa usando Django Rest Framework:
   - `GET /api/clientes/` — listar clientes ativos
   - `GET /api/clientes/?todos=1` — listar todos
   - `GET /api/clientes/{id}/` — detalhe de um cliente
   - `PATCH /api/clientes/{id}/inativar/` — inativar cliente
   - `PATCH /api/clientes/{id}/reativar/` — reativar cliente

7. **Frontend Angular** — projeto Angular separado que consome a API REST do backend, com tela de listagem, botões de inativar/reativar e filtro ativo/todos.

8. **CORS** — configurado `django-cors-headers` para permitir que o Angular (porta 4200) acesse o backend (porta 8000).

### Decisões tomadas

- **Simplicidade** — mantive a implementação direta e sem over-engineering, conforme orientado no teste.
- **DRF** — usei `ModelViewSet` porque já fornece CRUD completo com poucas linhas, e adicionei `@action` para inativar/reativar.
- **Filtro via query param** — escolhi `?todos=1` por ser simples e intuitivo, sem precisar de rotas extras.
- **Sem soft delete** — o campo `ativo` não exclui o cliente, apenas o oculta da listagem padrão, permitindo reativação.

### Como rodar o projeto completo

#### Backend (Django)
```bash
cd ms_test_oficial
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_clientes
python manage.py runserver
```
O backend roda em **http://localhost:8000**.

#### Frontend (Angular)
```bash
cd frontend
npm install
ng serve
```
O frontend roda em **http://localhost:4200**.

#### Rodar testes
```bash
cd ms_test_oficial
source .venv/bin/activate
python manage.py test
```