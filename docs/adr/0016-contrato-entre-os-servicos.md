---
id: adr-0016
titulo: "ADR-0016 — Contrato comum entre os serviços"
tipo: decisao
decisao: D16
status: aceita
data: 2026-11-03
decisor: Grupo (votação dos quatro integrantes)
itens_template: [12, 13, 14, 15]
areas: [A, B, C, D]
fontes: []
relacionados: [adr-0015]
---
# ADR-0016 — Contrato comum entre os serviços

- **Status:** aceita, como base provisória do RA2 · **Data:** 03/11/2026 · **Decisor:** grupo, por votação dos quatro integrantes

## Contexto

- A ADR-0015 dividiu o sistema em quatro microsserviços, um por integrante, e cada integrante escolhe a tecnologia do seu serviço. Para os serviços conversarem, todos precisam seguir as mesmas regras.
- Os critérios do RA2 pedem essas regras antes do item 13 (decisão B8 de `entregas/ra2-criterios-de-aceite.md`, seção 6).
- O grupo votou 22 perguntas em oito pontos, entre 01 e 03/11/2026. Os quatro responderam todas ([issue #137](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/137)).
- O resultado vale como verdade para escrever os itens 12 a 15. Ele pode ser revisto durante a implementação; nesse caso, uma ADR nova substitui esta.

## Opções consideradas

Cada pergunta teve de duas a quatro opções, mais "Outra". Ninguém usou "Outra". As opções e a explicação de cada uma estão na página da votação, ligada na issue #137.

## Decisão

Placar entre parênteses: votos da opção escolhida, de 4.

**1. Telas**

- Um único site. Cada integrante faz as telas da sua área (4).
- Framework: Angular (3; React teve 1).
- Design System próprio, a partir dos protótipos do Figma (4).
- `Jcliz` monta a estrutura inicial do site (4).

**2. Login e porta de entrada**

- Uma porta de entrada única (API Gateway) recebe todo acesso do site. A cada ação, ela consulta o Cadastro para saber se o usuário está ativo, como pede o RNF-1, e informa ao serviço quem é o usuário e seu perfil. Cada serviço confere se o perfil pode fazer a ação (4).
- Produto: Spring Cloud Gateway (2; NGINX e Kong tiveram 1 cada). Foi a opção mais votada, sem maioria.
- O Cadastro guarda usuários e senhas e emite o token de login. Não se usa produto pronto de identidade (4).
- `eduardofabrii` cuida da porta de entrada (4).

**3. Como o sistema conversa**

- Pedidos entre serviços: REST com JSON sobre HTTPS (RNF-3) (4).
- Site: REST, com GraphQL só nos painéis (4).
- Painel: as mudanças chegam por WebSocket, para cumprir os 5 s da meta do item 1 (4).
- A versão fica no endereço: `/v1/...` (4).
- A descrição de cada API, em OpenAPI, é gerada a partir do código (4).
- Uma recusa de regra de negócio volta com o motivo. Em uma falha técnica, quem chamou informa ao usuário que a ação não foi concluída.

**4. Mensageria**

- RabbitMQ, com filas duráveis e uma fila por serviço (4).
- No desenvolvimento, cada integrante roda a mensageria em Docker, na própria máquina (3; servidor compartilhado na nuvem teve 1).

**5. Avisos**

- Envelope próprio, igual para todos os avisos (4). Só muda o conteúdo de `dados`:

```json
{
  "id": "6f1c2a64-0d7b-4a54-9c2e-1b1f7a2d9e11",
  "tipo": "ChegadaRegistrada",
  "versao": 1,
  "ocorridoEm": "2026-11-28T17:02:00Z",
  "turnaroundId": "c7d1a3f0-52ab-4d0e-8f3e-5a0b6c9e2d44",
  "autorId": "a91e4b22-7c10-4f6d-b3a8-2e5d0c7f1b33",
  "origem": "execucao-em-solo",
  "causaId": "id do registro que causou este aviso",
  "dados": { "aibt": "2026-11-28T17:02:00Z" }
}
```

- `versao` permite mudar o formato sem quebrar os outros serviços (RNF-4). `causaId` permite reconstruir a linha do tempo pelos logs (RNF-24).
- A mensageria pode entregar o mesmo aviso duas vezes. Cada serviço guarda os `id` já processados e ignora o repetido (4).

**6. Horários**

- ISO 8601 em UTC, terminado em `Z`, em toda API e todo aviso (3; fuso local teve 1). A tela converte para o horário local. O registro feito sem conexão mantém o horário do celular (RNF-8), convertido para UTC. O `Z` indica o fuso do UTC, o que atende aos "horários com data e fuso" do RNF-4.

**7. Identificadores**

- UUID versão 4, gerado pelo serviço dono do dado. Os outros serviços guardam o identificador sem alterá-lo (4).

**8. Nomes**

Em português, sem acento no código (4).

| Elemento | Padrão | Exemplo |
|---|---|---|
| Classe | PascalCase, singular | `Turnaround`, `TarefaController` |
| Método e atributo | camelCase | `registrarInicio()` |
| Tabela e campo | snake_case, singular (4) | `tarefa`, `turnaround_id` |
| Campo em JSON | camelCase (4) | `turnaroundId` |
| Endereço de API | minúsculas, plural | `/v1/turnarounds/{id}/tarefas` |
| Aviso | PascalCase, no passado | `TarefaConcluida` |

## Consequências

- O item 13 usa esta convenção de nomes (critérios Y.4 e C13.9).
- O item 14 mostra os avisos com este envelope, os pedidos em REST e a porta de entrada no início das ações do site.
- O formato versionado vale para os avisos e as APIs de todos os serviços, e não só para os RFs que o RNF-4 cita.
- A porta de entrada e o Cadastro passam a ser necessários em toda ação. Se um deles cair, o sistema para.
- O site usa dois modelos de consulta: REST nas telas e GraphQL nos painéis. Os itens 13 e 14 definem quais painéis e quais serviços oferecem GraphQL.
- Cada integrante continua escolhendo linguagem, framework e banco do seu serviço, desde que siga este contrato.

---

## Ligações

- **Divisão em microsserviços:** [ADR-0015](0015-divisao-em-microsservicos.md)
- **Critérios do RA2:** [entregas/ra2-criterios-de-aceite.md](../../entregas/ra2-criterios-de-aceite.md)
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
