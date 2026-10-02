---
id: adb-safegate
titulo: "Ficha — ADB SAFEGATE (Safedock + Apron Manager)"
tipo: similar-ficha
secao_original: "3.2"
itens_template: [3]
areas: []
decisoes: []
fontes: [48, 49, 50, 61]
relacionados: [matriz-comparativa, lacunas-e-diferencial, similares]
status: vigente
atualizado: 2026-10-01
---
# Ficha 3 — ADB SAFEGATE (Safedock + Apron Manager / Intelligent AiPRON)

> Base de conhecimento do projeto · origem: seção 3.2 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).


| Campo | Registro |
|---|---|
| Produto e fornecedor | Safedock (A-VDGS, sistema avançado de guiagem visual de estacionamento), Apron Manager e a plataforma "Intelligent AiPRON". ADB SAFEGATE, sede em Machelen, **Bélgica** [Fato][61]. https://adbsafegate.com/what-we-do/apron/ [Fato][48][49][50] |
| Público-alvo | "airports, airlines, and ANSPs" (provedores de serviços de navegação aérea), em "over 3,000 airports in over 175 countries" [Fato][50]; no Apron Manager: centro de controle de operações do aeroporto (AOCC), controladores, pessoal de pátio, equipes de solo, tripulações e companhias [Fato][49]. |
| Problema que resolve | Gerir as atividades do pátio "from landing to takeoff" com automação e dados [Fato][50]. |
| Funcionalidades | Safedock guia a parada da aeronave [Fato][50]; recurso "Turn manager" que acompanha a atividade do turn e mede atrasos, prevê atrasos para atualizar o TOBT e fornece dados para marcos do CDM [Fato][48]; Apron Manager: alertas "before an aircraft arrives", monitoramento de equipamentos de solo e da posição, envio automático dos horários de block IN e OUT ao banco de voos, painel de KPIs por portão, suporte a A-CDM e acesso móvel [Fato][49]. *A página do Apron Manager traz no título extraído o nome "CORTEX Apron Manager".* |
| Como trata atrasos e exceções | Previsão de atraso → atualização do TOBT [Fato][48]; alertas antecipados [Fato][49]; análise de dados para "mitigate irregularities and create recommendations" [Fato][50]. |
| Fonte do dado operacional | Sensores do Safedock, câmeras, AODB e rastreamento de superfície (A-SMGCS e ADS-B, vigilância por transmissão automática de posição) [Fato][49]. |
| Métricas divulgadas — [Fato] (declarado pelo fornecedor) | previsão de "more than 8,000 Safedock systems" instalados até o fim de 2017 e "some 15 million aircraft dockings per year" [48]; turnarounds "faster, safer and more predictable" [49]. |
| Relação com A-CDM | Alimenta marcos do CDM e o TOBT; envia AIBT/AOBT automaticamente [Fato][48][49]. |
| O que vale incorporar [Inferência] | (1) Tratar o in-block e o off-block como **eventos** que disparam transições de estado (no MVP, registrados pelo operador ou simulados); (2) alerta **antes** da chegada quando o turnaround planejado não cabe (ligado à checagem EIBT + MTTT); (3) KPIs por posição. |
| O que fica fora do nosso escopo [Inferência] | Hardware de guiagem e sensores, A-SMGCS e integração física com o pátio. |

---

## Ligações

- **Itens da especificação:** [Item 3 — Visão do Produto](../../especificacao/03-visao-do-produto.md)
- **Relacionados:** [matriz-comparativa](matriz-comparativa.md), [lacunas-e-diferencial](lacunas-e-diferencial.md), [similares](README.md)
- **Fontes citadas:** 48, 49, 50, 61 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
