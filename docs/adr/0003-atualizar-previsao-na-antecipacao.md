---
id: adr-0003
titulo: "ADR-0003 — Antecipação de 5 min ou mais exige atualizar a previsão"
tipo: decisao
decisao: D3
status: aceita
data: 2026-10-01
decisor: Rodrigo Alves
itens_template: [1, 6, 7, 10]
areas: [C, D]
fontes: [7, 8, 9, 10, 11, 12, 13]
relacionados: [tolerancias-e-indicadores, previsibilidade-vs-velocidade, insumos-rfs, adr-0001]
---
# ADR-0003 — Antecipação de 5 min ou mais exige atualizar a previsão

- **Status:** aceita · **Data:** 01/10/2026 · **Decisor:** Rodrigo Alves · **Origem:** decisão D3 do [relatório de pesquisa](../../pesquisa/01-referencias-setor-e-similares.md) (seção 5)

## Contexto

O princípio do projeto é a aderência ao plano: terminar antes não é meta.

- **[Fato]** As regras de TOBT pedem atualização quando a previsão muda 5 min ou mais, nos dois sentidos [8][9][10][11][12].
- **[Fato]** O cartão de rampa dos aeroportos alemães manda comunicar qualquer desvio "regardless of whether the ground handling will end early or late" [13].
- **[Fato]** Heathrow mede a antecedência das atualizações do TOBT ("Late Updaters", "Predictability") [7].

## Opções consideradas

- **(a)** Nenhum evento quando uma tarefa ou o turnaround terminar antes do previsto.
- **(b)** Pedir atualização da previsão quando a antecipação chegar a 5 min.

## Decisão

**(b)**, seguindo o padrão de mercado: quando a projeção de prontidão ficar 5 min ou mais **antes** do TOBT vigente, o sistema pede ao Coordenador de Turnaround que atualize a previsão.

- **TOBT planejado:** definido na abertura do turnaround e fixo; é a régua da meta do objetivo 1 (ADR-0001).
- **TOBT vigente:** a última previsão informada pelo Coordenador de Turnaround; começa igual ao planejado e muda a cada atualização.
- **[Inferência]** Comparar com o vigente evita pedir a mesma atualização a cada recálculo: depois que o coordenador atualiza o TOBT, o pedido só volta se a projeção se afastar de novo 5 min ou mais, como nas regras que mandam atualizar quando a previsão muda 5 min ou mais [8][9].

## Consequências

- O Motor de Eventos gera um aviso de "antecipação ≥ 5 min" (não é alerta de risco nem desvio negativo).
- Regra de negócio nas áreas C (monitoramento) e D (replanejamento), com estórias que tenham critério DADO QUE/QUANDO/ENTÃO para o caso de antecipação.
- A métrica unilateral da [ADR-0001](0001-referencia-horario-tobt-mais-5-min.md) não muda.
- Revisão de 08/10/2026: a comparação passou do TOBT planejado para o TOBT vigente, alinhada ao RF-D6 e à US-D6; a meta continua medida contra o TOBT planejado.

---

## Ligações

- **Pesquisa:** [tolerancias-e-indicadores](../../pesquisa/topicos/tolerancias-e-indicadores.md), [previsibilidade-vs-velocidade](../../pesquisa/topicos/previsibilidade-vs-velocidade.md), [insumos-rfs](../../pesquisa/impacto/insumos-rfs.md)
- **Itens da especificação:** [Item 1 — 3 Objetivos](../../especificacao/01-3-objetivos.md), [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 7 — Estórias de Usuário](../../especificacao/07-estorias-de-usuario/00-item.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md)
- **Outras decisões:** [D1](0001-referencia-horario-tobt-mais-5-min.md)
- **Fontes citadas:** 7, 8, 9, 10, 11, 12, 13 (em [fontes.md](../../pesquisa/fontes.md))
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
