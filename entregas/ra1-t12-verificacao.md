# T12 — Revisão cruzada e verificação independente (#13)

Base revisada: `6d68a03a879fdecf9259e3f942e4bfea13ffc12b`, após os merges dos itens 10 e 11. Revisão técnica concluída; aprovação de outro integrante e merge seguem como gate do PR. A exportação de entrega e o envio no Canvas pertencem à #14.

Foram aplicados IDs definitivos e conferidas as relações de ponta a ponta. O [mapa de renumeração](ra1-renumeracao.md) preserva a consulta aos relatórios históricos. A matriz foi regenerada. A revisão independente encontrou e corrigiu: espera BPMN por sinais transitórios substituída por condições persistentes do turnaround; propagação de estados após replanejamento; emissão da loadsheet após embarque e bagagem, antes da junção geral; expansão e referência da norma ISO/IEC no item 8.

O [PDF de conferência](../output/pdf/ra1-conferencia.pdf) tem 206 páginas, sumário automático, declaração de IA e diagramas em folhas de dimensões próprias. É uma evidência da consolidação; o envio final não foi realizado. Os Markdown e fontes dos diagramas permanecem editáveis.

Verificações: `python scripts/verificar_revisao.py` (zero erros); `git diff --check`; reprodução idêntica da matriz; renderização PlantUML 1.2026.0 e BPMN com bpmn-js 18.9.1; renderização e inspeção visual do PDF. Verificadores independentes revisaram itens 1–5/PDF, 6–8 e 9–11. O grafo foi consultado, sem regeneração; suas relações foram confirmadas nos Markdown atuais.

## Evidência por critério

| ID | Status | Evidência |
|---|---|---|
| X.1 | Atendido | PDF com itens 1–11 em ordem, quadros e Apêndice A após item 11. |
| X.2 | Atendido | Capa com produto, quatro autores e 2026. |
| X.3 | Atendido | Textos personalizados em preto; inspeção visual e de cores no PDF. |
| X.4 | Atendido | Orientações e avisos do template ausentes. |
| X.5 | Atendido | Exemplos substituídos por conteúdo do domínio; login conforme ADR-0010. |
| X.6 | Atendido | Sumário automático gerado em múltiplas passagens e páginas conferidas. |
| X.7 | Atendido | Declaração na página 2: Claude Code 2.1.296 e Codex (GPT-6), motivos e responsabilidade. |
| X.8 | Atendido | Todas as áreas superam quatro RFs, estórias, RNFs e casos de uso. |
| X.9 | Atendido | Nome do produto consistente nos quadros e capa. |
| X.10 | Atendido | Diagramas em folhas com dimensões próprias, sem cortes e com texto legível. |
| C01.1 | Atendido | 3 objetivos numerados no item 1. |
| C01.2 | Atendido | Objetivos com resultados observáveis e métricas explícitas. |
| C01.3 | Atendido | Problema, valor e meta de sucesso descritos nos três objetivos. |
| C01.4 | Atendido | Objetivos relacionados à visão e à coluna OBJETIVO dos 44 RFs. |
| C02.1 | Atendido | Quatro quadrantes completos no item 2. |
| C02.2 | Atendido | Quadrantes É/Não é/Faz/Não faz: 7/5/10/7 itens. |
| C02.3 | Atendido | Revisão independente entre quadrantes e itens 1, 3 e 6–11. |
| C02.4 | Atendido | Exclusões de voos, tripulação, financeiro e integração real com ATC preservadas. |
| C03.1 | Atendido | 5 problemas e 5 expectativas no quadro A. |
| C03.2 | Atendido | Correspondência entre problemas e expectativas verificada. |
| C03.3 | Atendido | Todos os cinco campos do quadro B preenchidos. |
| C03.4 | Atendido | Meta-valor e diferencial com resultados verificáveis. |
| C03.5 | Atendido | Revisão independente dos itens 1–3 sem contradições. |
| C04.1 | Atendido | XML BPMN 2.0 e exportações PNG/SVG no item 4. |
| C04.2 | Atendido | Processo explicitamente TO BE. |
| C04.3 | Atendido | Eventos inicial e final presentes. |
| C04.4 | Atendido | Atividades nomeadas por ações do processo. |
| C04.5 | Atendido | Condições explícitas nos gateways; condições persistentes para pré-requisitos locais. |
| C04.6 | Atendido | Raias coerentes com os responsáveis do item 5. |
| C04.7 | Atendido | Eventos operacionais e alertas representados. |
| C04.8 | Atendido | Caminho principal conferido; exportação integral e página de diagrama no PDF. |
| C04.9 | Atendido | Processo atende a orquestração, paralelismo e controle da visão. |
| C05.1 | Atendido | 5 atores concretos: quatro humanos e Motor de Eventos. |
| C05.2 | Atendido | Descrições de responsabilidades no item 5. |
| C05.3 | Atendido | Relação de cada ator com processo e sistema explícita. |
| C05.4 | Atendido | Papéis revisados sem sobreposição indevida. |
| C05.5 | Atendido | Nomes consistentes entre artefatos; Usuário abstrato conforme ADR-0010. |
| C06.1 | Atendido | 44 RFs; por área A/B/C/D: 13/8/14/9. |
| C06.2 | Atendido | RF-1 a RF-44 sem lacunas ou duplicatas. |
| C06.3 | Atendido | 44 ações verificáveis revisadas independentemente. |
| C06.4 | Atendido | Coluna ATOR preenchida nos 44 RFs. |
| C06.5 | Atendido | Coluna OBJETIVO preenchida nos 44 RFs. |
| C06.6 | Atendido | SPRINT preenchida nos 44 RFs. |
| C06.7 | Atendido | Justificativa de priorização no item 6. |
| C06.8 | Atendido | Cobertura de orquestração, paralelismo, estados, atraso, caminho crítico, painel, alertas e recursos. |
| C07.1 | Atendido | 44 estórias; uma por RF. |
| C07.2 | Atendido | 44 estórias em COMO/POSSO/PARA. |
| C07.3 | Atendido | US001–US044 vinculadas a RF-1–RF-44; bijeção validada. |
| C07.4 | Atendido | Contagem automatizada confirma pelo menos dois critérios por estória. |
| C07.5 | Atendido | Critérios completos em DADO QUE/QUANDO/ENTÃO; resultados observáveis. |
| C07.6 | Atendido | Caminho principal e variações/erros revisados por estória. |
| C07.7 | Atendido | Relações com atores, RFs e casos de uso revisadas. |
| C08.1 | Atendido | 24 RNFs; por área A/B/C/D: 6/4/8/6. |
| C08.2 | Atendido | RNF-1 a RNF-24 sem lacunas ou duplicatas. |
| C08.3 | Atendido | 24 RNFs classificados pela ISO/IEC 25010:2011; fonte [103]. |
| C08.4 | Atendido | Medidas e limites objetivos nos 24 RNFs. |
| C08.5 | Atendido | Desempenho, segurança, confiabilidade, usabilidade e manutenibilidade cobertos. |
| C08.6 | Atendido | RFs aplicáveis citados no texto de cada RNF; nenhuma tabela Base. |
| C09.1 | Atendido | Fronteira com Aircraft Turnaround Orchestration System. |
| C09.2 | Atendido | Atores concretos do item 5 e Usuário abstrato. |
| C09.3 | Atendido | 37 casos de uso cobrem os 44 RFs, conforme matriz. |
| C09.4 | Atendido | Generalização dos quatro atores humanos para Usuário. |
| C09.5 | Atendido | Include/extend conferidos na revisão independente. |
| C09.6 | Atendido | 37 nomes do diagrama iguais aos títulos do item 10; validador automatizado. |
| C09.7 | Atendido | PNG/SVG regenerados e diagrama legível no PDF. |
| C10.1 | Atendido | 37 especificações; por área A/B/C/D: 13/8/7/9. |
| C10.2 | Atendido | 10 campos preenchidos nas 37 especificações. |
| C10.3 | Atendido | 42 protótipos referenciados, verificados na consolidação do item 10. |
| C10.4 | Atendido | 37 fluxos básicos completos e numerados. |
| C10.5 | Atendido | 119 fluxos alternativos, ao menos um por caso. |
| C10.6 | Atendido | 122 fluxos de exceção, ao menos um por caso. |
| C10.7 | Atendido | Passos observáveis revisados independentemente. |
| C10.8 | Atendido | 37 nomes e atores correspondentes ao diagrama; nomes também validados por script. |
| C10.9 | Atendido | Regras cruzadas com os RFs e critérios das estórias. |
| C10.10 | Atendido | IDs definitivos dos RFs presentes nas regras/fluxos; cobertura integral na matriz. |
| C11.1 | Atendido | Fluxo principal em 11-atividades.puml. |
| C11.2 | Atendido | Variações nos quatro diagramas de atividades. |
| C11.3 | Atendido | Guardas explícitas nos nós de decisão. |
| C11.4 | Atendido | Fork/join em 11-atividades-paralelas; loadsheet após embarque e bagagem. |
| C11.5 | Atendido | Partições coerentes com os atores responsáveis. |
| C11.6 | Atendido | Nós inicial/final, decisões e paralelismo UML conferidos. |
| C11.7 | Atendido | Quatro PNG/SVG regenerados; monitoramento propaga estados após replanejamento. |
| K.1 | Atendido | Atores cruzados nos itens 4–11, conforme ADR-0009/0010. |
| K.2 | Atendido | 44 pares RF/US exclusivos, sem referências inexistentes. |
| K.3 | Atendido | Matriz cobre 44 RFs por 37 casos presentes no diagrama. |
| K.4 | Atendido | 37 títulos iguais entre especificações e diagrama. |
| K.5 | Atendido | Critérios das estórias cruzados com regras e fluxos; correções de atividades incorporadas. |
| K.6 | Atendido | Três objetivos atendidos pelos RFs e refletidos no item 3. |
| K.7 | Atendido | Anti-escopo preservado nos RFs, estórias e casos de uso. |
| K.8 | Atendido | Raias BPMN/UML conferidas com item 5. |
| K.9 | Atendido | Contagem por comando: 44 RF, 44 US, 24 RNF, 37 UC; ≥2 critérios por US. |
| K.10 | Atendido | X.1–X.10 conferidos no PDF consolidado de conferência. |
| K.11 | Atendido | CONTEXT e ADRs preservados; siglas expandidas e fontes setoriais citadas nos itens. |
| K.12 | Atendido | Consulta GitHub: nenhuma issue aberta com rótulo pendencia-cruzada. |
| K.13 | Atendido | Matriz regenerada após renumeração: 0 lacunas; reprodução idêntica validada. |
