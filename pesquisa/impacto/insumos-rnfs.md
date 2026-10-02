---
id: insumos-rnfs
titulo: "Insumos para os RNFs (seção 4.4)"
tipo: impacto
secao_original: "4.4"
itens_template: [8]
areas: [A, B, C, D]
decisoes: [D1]
fontes: [2, 3, 5, 13, 36, 40, 43, 46, 51, 53, 54]
relacionados: [tolerancias-e-indicadores, referencias-iata, impacto-por-item]
status: vigente
atualizado: 2026-10-01
---
# Insumos para os RNFs (seção 4.4)

> Base de conhecimento do projeto · origem: seção 4.4 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).

> **Decisões vigentes (prevalecem sobre o texto abaixo):** [D1 — Referência de horário: TOBT planejado + 5 min, unilateral](../../docs/adr/0001-referencia-horario-tobt-mais-5-min.md).
>
> Precisão de minuto e regra de arredondamento sustentam a régua TOBT + 5 min (D1).


| Exigência | Origem | Característica ISO/IEC 25010 sugerida [Inferência] |
|---|---|---|
| Atualização "em tempo real" do painel e dos alertas; meta numérica a definir (ex.: ≤5 s p95) | [Fato] fornecedores falam em "real time" [40][51][54]; número = meta interna | Eficiência de desempenho (comportamento no tempo) |
| Horários registrados com precisão de minuto, no mínimo, e regra de arredondamento explícita | [Fato] "5:59 is acceptable while 6:00 is not" [3] | Adequação funcional (correção) |
| Trilha de auditoria de toda mudança de estado (quem, quando, o quê) | [Fato] marcos registrados com responsável [2]; auditorias ISAGO [36] | Segurança (responsabilização / não repúdio) |
| Acesso por papel; proteção de dados pessoais de funcionários (LGPD — Lei Geral de Proteção de Dados Pessoais) | [Fato] visões e acessos por papel [51]; LGPD = exigência legal brasileira [Inferência] | Segurança (confidencialidade) |
| Uso em dispositivo móvel no pátio | [Fato] apps móveis para quem executa [43][46]; checagens no pátio em TOBT − 15 e TOBT − 3 [13] | Usabilidade / Portabilidade |
| Disponibilidade durante toda a janela de operação do aeroporto | [Fato] suporte 24/7 citado pela SITA [53]; valor a definir | Confiabilidade (disponibilidade) |
| Interface de dados padronizada para troca com terceiros | [Fato] a IATA recomenda "a common API" para acesso a dados de A-CDM [5] | Compatibilidade (interoperabilidade) |
| Continuar registrando com conexão instável no pátio | [Inferência] sem fonte; risco típico de uso móvel em área aberta | Confiabilidade (tolerância a falhas) |
| Regras de tolerância e gatilhos de alerta parametrizáveis (variáveis locais) | [Fato] vários valores são "local variable" no A-CDM [2] | Manutenibilidade (modificabilidade) |

---

## Ligações

- **Decisões:** [D1](../../docs/adr/0001-referencia-horario-tobt-mais-5-min.md)
- **Itens da especificação:** [Item 8 — Requisitos Não Funcionais](../../especificacao/08-requisitos-nao-funcionais/00-item.md)
- **Áreas do plano RA1:** [Área A — Acesso e planejamento](../../especificacao/06-requisitos-funcionais/area-a.md), [Área B — Execução em solo](../../especificacao/06-requisitos-funcionais/area-b.md), [Área C — Monitoramento](../../especificacao/06-requisitos-funcionais/area-c.md), [Área D — Exceções e liberação](../../especificacao/06-requisitos-funcionais/area-d.md) (divisão em [entregas/ra1-tarefas.md](../../entregas/ra1-tarefas.md), tabela 1.2)
- **Relacionados:** [tolerancias-e-indicadores](../topicos/tolerancias-e-indicadores.md), [referencias-iata](../topicos/referencias-iata.md), [impacto-por-item](impacto-por-item.md)
- **Fontes citadas:** 2, 3, 5, 13, 36, 40, 43, 46, 51, 53, 54 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
