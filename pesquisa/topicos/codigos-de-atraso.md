---
id: codigos-de-atraso
titulo: "Códigos de atraso (P1.8)"
tipo: pesquisa-topico
secao_original: "2.8"
itens_template: [2, 6, 7, 10]
areas: [B, D]
decisoes: [D6]
fontes: [1, 16, 37, 38, 62]
relacionados: [atividades-e-dependencias, referencias-iata, insumos-rfs]
status: vigente
atualizado: 2026-10-01
---
# Códigos de atraso (P1.8)

> Base de conhecimento do projeto · origem: seção 2.8 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).

> **Decisões vigentes (prevalecem sobre o texto abaixo):** [D6 — Códigos de atraso: tabela completa da ANAC (72 códigos)](../../docs/adr/0006-codigos-de-atraso-tabela-anac.md).
>
> O projeto usa a tabela completa da ANAC (72 códigos), que substitui a inferência do fim desta página sobre usar só o grupo 31–39 (D6).


**[Fato][16]** O padrão de mercado são os códigos de atraso de dois dígitos da IATA (AHM 730), reproduzidos no anexo do relatório CODA da EUROCONTROL. A EUROCONTROL agrupa as causas em "Airline, Airport, ATFM, Weather, Other" e "Reactionary". **[Fato][1]** Em aeroportos A-CDM, "the target off-block time (TOBT) values reflect any delays that can be attributed to the aircraft operator (AO) or to the ground handling operations."

Códigos mais ligados ao turnaround (texto literal do anexo [16]):

| Código | Descrição IATA (original) | Responsabilidade do turnaround? [Inferência] |
|---|---|---|
| 15 (PH) | BOARDING, discrepancies and paging, missing checked-in passenger | Sim (embarque) |
| 17 (PC) | CATERING ORDER, late or incorrect order given to supplier | Parcial (pedido é da companhia) |
| 18 (PB) | BAGGAGE PROCESSING, sorting etc. | Parcial (antes da rampa) |
| 19 (PW) | REDUCED MOBILITY, boarding deboarding of passengers with reduced mobility | Sim |
| 31 (GD) | AIRCRAFT DOCUMENTATION LATE INACCURATE, weight and balance | Sim (*load control*) |
| 32 (GL) | LOADING UNLOADING, bulky, special load, cabin load, lack of loading staff | Sim |
| 33 (GE) | LOADING EQUIPMENT, lack of or breakdown, lack of staff | Sim (recurso) |
| 34 (GS) | SERVICING EQUIPMENT, lack of or breakdown, lack of staff, e.g. steps | Sim (recurso) |
| 35 (GC) | AIRCRAFT CLEANING | Sim |
| 36 (GF) | FUELLING DEFUELLING, fuel supplier | Sim |
| 37 (GB) | CATERING, late delivery or loading | Sim |
| 38 (GU) | ULD, lack of or serviceability (ULD = *unit load device*, contêiner/palete de carga) | Sim |
| 39 (GT) | TECHNICAL EQUIPMENT, lack of or breakdown, lack of staff, e.g. pushback | Sim (recurso) |
| 41 (TD) | AIRCRAFT DEFECTS | Parcial (manutenção) |
| 42 (TM) | SCHEDULED MAINTENANCE, late release | Parcial (manutenção) |
| 43 (TN) | NON-SCHEDULED MAINTENANCE, special checks and or additional works beyond normal maintenance schedule | Parcial (manutenção) |
| 52 (DG) | DAMAGE DURING GROUND OPERATIONS, collisions, loading off-loading damage | Sim (exceção de segurança) |
| 63 (FT) | LATE CREW BOARDING OR DEPARTURE PROCEDURES, other than connection and standby (flight deck or entire crew) | Não (tripulação) |
| 66 (FL) | LATE CABIN CREW BOARDING OR DEPARTURE PROCEDURES, other than connection and standby | Não (tripulação) |
| 75 (WI) | DE-ICING OF AIRCRAFT, removal of ice and or snow, frost prevention excluding unserviceability of equipment | Parcial (degelo fora do MVP) |
| 77 (WG) | GROUND HANDLING IMPAIRED BY ADVERSE WEATHER CONDITIONS | Parcial |
| 87 (AF) | AIRPORT FACILITIES, parking stands, ramp congestion, lighting, buildings | Não (aeroporto) |
| 93 (RA) | AIRCRAFT ROTATION, late arrival of aircraft from another flight | Não — atraso reacionário que **chega** ao turnaround |

- **[Fato][37]** A IATA tem um novo esquema de códigos, o **AHM 732**, divulgado em webinar próprio. **[Fato][38]** (fonte de fornecedor, blog Cosmos, 22/07/2025) O AHM 732 troca os dois dígitos por três letras — processo, motivo e parte envolvida (*stakeholder*) — e, segundo o blog, os códigos AHM 730/731 valem "until the 43rd edition", com o AHM 732 virando padrão a partir da 44ª edição. *O cronograma não foi confirmado em documento oficial da IATA.*
- **[Inferência]** Para o MVP, os códigos de dois dígitos do grupo 31–39 (mais 15, 19 e 52) cobrem as causas atribuíveis ao turnaround e têm texto público verificável. O código 93 é útil como causa **de entrada** (aeronave chegou atrasada), que o sistema registra mas não trata.
- **Decisão D6 (vigente, substitui a inferência acima):** **[Fato][62]** a Portaria nº 55/SPO/SSA, de 06/08/2026, altera a Portaria nº 791/SSO/2012, que trata do registro dos motivos de atraso e cancelamento de voos, e institui nova tabela: **72 códigos** em 12 categorias, só com siglas de duas letras e descrições em português. **[Inferência]** As siglas e as categorias são as mesmas da IATA AHM 730 (ex.: GC limpeza, GF combustível, GB catering, RA aeronave que chegou atrasada), comparando [62] com [16]. O projeto usa os 72 códigos, sem recorte. O AHM 732 não foi adotado pela ANAC.
- **Registro da leitura de [62] (01/10/2026):** ementa "Altera a Portaria nº 791/SSO, de 26 de abril de 2012, para atualizar os procedimentos de registro dos motivos de atraso e cancelamento de voos"; publicada no DOU de 11/08/2026, Seção 1, págs. 69–70, com vigência na data da publicação; art. 2º, § 3º: "O registro dos motivos e tempos de atraso deve utilizar como referência o horário de partida previsto do voo"; anexo com as colunas CÓDIGO, CATEGORIA e DESCRIÇÃO PARA O INFOVOO/SRV e as categorias: outros motivos da empresa de transporte aéreo; passageiros e bagagens; carga e mala postal; aeronave e serviços de rampa; ordem técnica e equipamentos da aeronave; danos à aeronave; falha em sistemas de processamento de dados ou equipamentos automatizados; operações de voo e tripulação; condições meteorológicas; restrições por gerenciamento do fluxo de tráfego aéreo; operador do aeroporto e autoridades governamentais; atraso em cadeia / motivos diversos.

---

## Ligações

- **Decisões:** [D6](../../docs/adr/0006-codigos-de-atraso-tabela-anac.md)
- **Itens da especificação:** [Item 2 — É / Não é / Faz / Não faz](../../especificacao/02-e-nao-e-faz-nao-faz.md), [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 7 — Estórias de Usuário](../../especificacao/07-estorias-de-usuario/00-item.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md)
- **Áreas do plano RA1:** [Área B — Execução em solo](../../especificacao/06-requisitos-funcionais/area-b.md), [Área D — Exceções e liberação](../../especificacao/06-requisitos-funcionais/area-d.md) (divisão em [entregas/ra1-tarefas.md](../../entregas/ra1-tarefas.md), tabela 1.2)
- **Relacionados:** [atividades-e-dependencias](atividades-e-dependencias.md), [referencias-iata](referencias-iata.md), [insumos-rfs](../impacto/insumos-rfs.md)
- **Fontes citadas:** 1, 16, 37, 38, 62 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
