# Requisitos - [Nome do sistema] ([Tema])

## 1. Objetivo

O sistema tem como objetivo [explicar o que o sistema fará], atendendo principalmente [público ou usuário].

## 2. Atores

- [Ator 1]
- [Ator 2]
- Administrador

## 3. Requisitos funcionais — escopo mínimo

- RF01: O sistema deve cadastrar [entidade principal].
- RF02: O sistema deve permitir consultar [informação].
- RF03: O sistema deve enviar uma mensagem de WhatsApp quando [evento].
- RF04: O sistema deve registrar as mensagens enviadas no banco de dados.
- RF05: O sistema deve receber o status de entrega das mensagens por webhook.
- RF06: O sistema deve consultar a API [nome da segunda API] para [finalidade].

## 4. Requisitos não funcionais

- RNF01: A API própria deve ser desenvolvida em [Node.js ou Python].
- RNF02: O banco de dados deve utilizar PostgreSQL.
- RNF03: As alterações do banco devem ser registradas por migrations versionadas.
- RNF04: A aplicação e o banco devem ser executados com Docker Compose.
- RNF05: Senhas, tokens e credenciais devem ser armazenados em variáveis de ambiente.
- RNF06: O projeto deve utilizar Git e GitHub para versionamento.

## 5. Mensagens que o sistema envia

| Evento | Destinatário | Conteúdo resumido |
|---|---|---|
| [Evento 1] | [Destinatário] | [Mensagem enviada] |
| [Evento 2] | [Destinatário] | [Mensagem enviada] |

## 6. Entidades do banco — previsão inicial

### [Entidade principal]

- id
- [campo]
- [campo]
- created_at
- updated_at

### Mensagem

- id
- destinatario
- conteudo
- status
- data_envio

## 7. Fora do escopo

Neste semestre, o sistema não terá:

- [Funcionalidade que não será desenvolvida]
- [Integração que não será implementada]
- [Limitação definida pelo grupo]