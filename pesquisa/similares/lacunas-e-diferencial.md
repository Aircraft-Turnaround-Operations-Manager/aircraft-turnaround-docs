---
id: lacunas-e-diferencial
titulo: "Lacunas e diferencial possível (seção 3.4)"
tipo: similar-sintese
secao_original: "3.4"
itens_template: [2, 3]
areas: []
decisoes: [D7]
fontes: [2, 42, 63, 64]
relacionados: [matriz-comparativa, impacto-por-item, caminho-critico]
status: vigente
atualizado: 2026-10-01
---
# Lacunas e diferencial possível (seção 3.4)

> Base de conhecimento do projeto · origem: seção 3.4 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).

> **Decisões vigentes (prevalecem sobre o texto abaixo):** [D7 — Dados registrados pelo operador, inclusive QR Code lido pelo celular](../../docs/adr/0007-dados-do-operador-e-qr-code.md).
>
> A D7 ajustou o DF3 (o operador pode usar a câmera do celular para ler QR Code) e acrescentou o DF5.


**Lacunas observadas [Inferência]** (com base na matriz 3.3):

1. Nenhuma das cinco fontes públicas documenta um **bloqueio formal da liberação** enquanto houver tarefa obrigatória pendente ou exceção aberta.
2. Só o INFORM documenta propagação para processos dependentes, e nenhum produto documenta **caminho crítico explícito** mostrado por turnaround.
3. Os produtos de visão computacional e sensores (Assaia, ADB SAFEGATE) exigem câmeras ou sensores instalados no pátio. Os de plataforma A-CDM (Veovo, SITA) focam no aeroporto e no sequenciamento de partidas, não em quem executa cada tarefa.
4. O mais próximo do nosso núcleo é o INFORM GroundStar (TurnManager + TeamWork), que vem junto com planejamento, escala e custos (fora do nosso escopo).

**Diferencial possível, em linguagem verificável (insumo para o critério C03.4) [Inferência]:**

- **DF1.** Cada turnaround é um grafo de tarefas com dependências e estados; a cada registro, o sistema recalcula o caminho crítico e a projeção de prontidão e os mostra no painel em até X segundos. *Verificável por teste de aceitação.*
- **DF2.** A transição para "Liberado" é bloqueada enquanto houver tarefa obrigatória pendente ou exceção aberta. *Verificável por teste e pela métrica "0 liberações com pendência".*
- **DF3.** Funciona com registro do operador (web/app), inclusive leitura de QR Code pela câmera do celular, sem sensores da aeronave, câmeras fixas no pátio ou integração com ATC (D7). *Verificável pela lista de requisitos de implantação.*
- **DF5.** Confirmação de tarefas por leitura de QR Code no celular do operador, como a limpeza da cabine por assento, fileira ou zona, atualizando o andamento do turnaround (D7). Não encontrado nas fontes consultadas [42][63][64]. *Verificável por demonstração.*
- **DF4.** Mede a aderência com a mesma régua do setor: prontidão até TOBT + 5 min (T8, [2]). *Verificável pelo cálculo da métrica.*

Para a redação final, recomenda-se escrever "não documentado nas fontes públicas dos similares analisados", e não "único no mercado".

---

## Ligações

- **Decisões:** [D7](../../docs/adr/0007-dados-do-operador-e-qr-code.md)
- **Itens da especificação:** [Item 2 — É / Não é / Faz / Não faz](../../especificacao/02-e-nao-e-faz-nao-faz.md), [Item 3 — Visão do Produto](../../especificacao/03-visao-do-produto.md)
- **Relacionados:** [matriz-comparativa](matriz-comparativa.md), [impacto-por-item](../impacto/impacto-por-item.md), [caminho-critico](../topicos/caminho-critico.md)
- **Fontes citadas:** 2, 42, 63, 64 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
