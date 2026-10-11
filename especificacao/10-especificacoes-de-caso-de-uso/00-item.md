# 10 ESPECIFICAÇÕES DE CASO DE USO

**PRODUTO:** Aircraft Turnaround Orchestration System

Esta seção reúne 37 especificações de caso de uso: 13 de acesso e planejamento (área A), 8 de execução em solo (área B), 7 de monitoramento (área C) e 9 de exceções e liberação (área D). Os nomes, atores e relacionamentos correspondem ao diagrama geral do item 9. Cada especificação apresenta nome, atores, descrição, pré-condições, pós-condições, regras de negócio, protótipos de tela, fluxo básico, fluxos alternativos e fluxos de exceção.

Os 37 casos de uso cobrem os 44 requisitos funcionais e suas estórias; um caso de uso pode reunir requisitos relacionados. A relação entre esses artefatos está no Apêndice A — Matriz de rastreabilidade. Os identificadores por área são provisórios e serão renumerados na revisão final, conforme a ADR-0011.

**Siglas usadas neste item.** A tomada de decisão colaborativa em aeroportos (A-CDM) [2][4] fornece os marcos de referência: horário programado de chegada à posição (SIBT), horário programado de saída da posição (SOBT), horário estimado de chegada à posição (EIBT), horário real de chegada à posição (AIBT), início real do atendimento em solo (ACGT), início real do embarque (ASBT), fim real do atendimento em solo (AEGT), horário real de prontidão (ARDT), horário real de saída da posição (AOBT), horário-alvo de prontidão (TOBT) e tempo mínimo de turnaround (MTTT). O controle de tráfego aéreo (ATC) permanece fora do escopo. As causas de atraso usam a tabela da Agência Nacional de Aviação Civil (ANAC) [62]. Os pontos de confirmação usam código de resposta rápida (QR Code), lido pela câmera do celular (ADR-0007). A regra de abastecimento cita o Regulamento Brasileiro da Aviação Civil (RBAC) nº 91 e a unidade auxiliar de energia (APU) [27].

Fontes citadas: [2], [4], [27] e [62], conforme a numeração de `pesquisa/fontes.md`.
