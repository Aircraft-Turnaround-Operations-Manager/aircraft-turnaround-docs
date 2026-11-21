---
id: adr-0024
titulo: "ADR-0024 — Canvas de Design como fonte única das telas"
tipo: decisao
decisao: D24
status: proposta
data: 2026-11-21
decisor: Grupo (aprovação dos integrantes no pull request)
itens_template: [10]
areas: [A, B, C, D]
fontes: []
relacionados: [adr-0016, adr-0007, adr-0010]
---
# ADR-0024 — Canvas de Design como fonte única das telas

- **Status:** proposta: passa a aceita quando os outros integrantes aprovarem o pull request · **Data:** 21/11/2026 · **Decisor:** grupo, pela aprovação do pull request · **Altera:** [ADR-0016](0016-contrato-entre-os-servicos.md), ponto 1 ("Design System próprio, a partir dos protótipos do Figma")

## Contexto

- A ADR-0016, ponto 1, votada pelos quatro integrantes, diz que o Design System próprio parte dos protótipos do Figma (arquivo `aircraft`).
- Em 20/11/2026, um inventário comparou as 42 imagens de tela do PDF do RA1, que são as imagens de `especificacao/10-especificacoes-de-caso-de-uso/prototipos/`, com os frames do Figma. O resultado está no [inventário das telas](../../entregas/inventario-prototipos.md). Resultado:
  - 33 imagens são iguais ao Figma;
  - 2 divergem do Figma, porque foram melhoradas direto no PNG (UC20 e UC32);
  - 7 não existem no Figma: as telas da área C (UC22 a UC28), geradas localmente junto com o texto (commits `144bdd5` e `18a2ddb`).
- Com duas fontes que não batem, uma decisão de especificação chegou a ser tomada em cima de uma imagem que ninguém desenhou no Figma: a aba "Encerrados hoje" do UC26.
- Na mesma data, todas as telas foram reconstruídas num canvas de Design no Claude, compartilhado com os quatro integrantes. São 43 telas do Figma, conferidas contra o frame, e as 7 que estavam fora dele, marcadas com a origem: [Protótipos de tela — Aircraft Turnaround Orchestration System](https://claude.ai/artifact/79Tw5VSVMVEracfZeYMGaX).

## Opções consideradas

- **(a)** Manter o Figma como fonte e desenhar nele as 7 telas que faltam. O canvas seria descartado.
- **(b)** Manter as duas fontes, com o PNG do repositório como palavra final. A divergência continuaria.
- **(c)** Adotar o canvas como fonte única: o Figma fica congelado como histórico, e o PNG passa a ser só a exportação do canvas.

## Decisão

**(c)**:

1. **Fonte única.** O layout de toda tela do projeto está no canvas [Protótipos de tela — Aircraft Turnaround Orchestration System](https://claude.ai/artifact/79Tw5VSVMVEracfZeYMGaX). Tela nova e ajuste de tela existente se fazem nele.
2. **Figma congelado.** O arquivo `aircraft` do Figma deixa de ser atualizado e fica só como histórico do RA1.
3. **Imagens do documento.** Cada PNG de `especificacao/10-especificacoes-de-caso-de-uso/prototipos/` é a exportação de uma tela do canvas, com o mesmo nome. Ninguém gera imagem de tela na própria máquina. Quando uma tela muda no canvas, a imagem é exportada de novo, no mesmo pull request que muda o texto que a cita.
4. **Dono da tela.** Cada integrante muda as telas da sua área. Para mudar a tela de outra área, é preciso a concordância do dono da área, registrada na issue ou no pull request.
5. **Origem marcada.** O título de cada tela no canvas diz o caso de uso e a origem. A legenda do canvas diz de onde veio cada grupo de telas.
6. **Design System.** O Design System próprio da ADR-0016, ponto 1, parte das telas do canvas, e não mais do Figma. O resto do ponto 1 não muda.

## Consequências

- O Claude de cada integrante segue a regra 11 do `AGENTS.md`: lê e muda telas só no canvas, e nunca usa o Figma nem gera imagem local.
- As telas continuam provisórias. Servem à especificação e não são a interface final, como já vale para os protótipos do RA1.
- O canvas fica fora do repositório, então o histórico de cada mudança de tela fica no próprio canvas. No repositório ficam as imagens exportadas e o texto.
- Quem não tem acesso ao canvas não consegue mudar telas. O acesso é dado pelo dono do canvas (Rodrigo Alves).
- A ADR-0016, ponto 1, ganha a nota de que a fonte das telas mudou por esta ADR.

---

## Ligações

- **Contrato entre os serviços (ponto 1, telas):** [ADR-0016](0016-contrato-entre-os-servicos.md)
- **Regra para quem escreve (pessoas e IAs):** [AGENTS.md](../../AGENTS.md), regra 11
- **Especificações de caso de uso (item 10):** [00-item.md](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md)
- **Inventário das telas (origem de cada uma):** [entregas/inventario-prototipos.md](../../entregas/inventario-prototipos.md)
- **Índice das decisões:** [README.md](README.md)
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
