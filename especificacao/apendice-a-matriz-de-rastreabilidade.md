# APÊNDICE A — MATRIZ DE RASTREABILIDADE

A matriz cruza os requisitos funcionais (item 6) com os objetivos (item 1), os atores (item 5), as estórias de usuário (item 7), os casos de uso (itens 9 e 10) e os requisitos não funcionais (item 8). Ela mostra que todo requisito funcional atende a um objetivo e tem estória e caso de uso, e que todo requisito não funcional se aplica a requisitos funcionais definidos (ADR-0012).

As tabelas abaixo são **geradas** pelo script `scripts/gerar_matriz_rastreabilidade.py` a partir dos arquivos de área. Não edite o trecho entre os marcadores: altere os requisitos, as estórias ou os casos de uso e rode o script de novo.

<!-- matriz:inicio -->
### A.1 Requisitos funcionais × objetivos, atores, estórias, casos de uso e RNFs

| RF | Objetivo | Ator / usuário | Estória | Caso(s) de uso | RNFs aplicáveis |
|---|---|---|---|---|---|
| RF-B1 | Obj. 2 | Operador de Solo/Rampa | US-B1 | UC-B1, UC-B8 | RNF-B1 |
| RF-B2 | Obj. 1 e 2 | Operador de Solo/Rampa | US-B2 | UC-B2, UC-B8 | RNF-B1, RNF-B2 |
| RF-B3 | Obj. 1 e 2 | Operador de Solo/Rampa | US-B3 | UC-B3, UC-B6, UC-B8 | RNF-B1, RNF-B2 |
| RF-B4 | Obj. 2 e 3 | Operador de Solo/Rampa | US-B4 | UC-B4, UC-B8 | RNF-B1, RNF-B2, RNF-D4 |
| RF-B5 | Obj. 2 e 3 | Operador de Solo/Rampa | US-B5 | UC-B5, UC-B8 | RNF-B1, RNF-B2 |
| RF-B6 | Obj. 2 | Operador de Solo/Rampa | US-B6 | UC-B3, UC-B6, UC-B8 | RNF-B1, RNF-B2 |
| RF-B7 | Obj. 1 | Motor de Eventos | US-B7 | UC-B5, UC-B7, UC-B8 | — |
| RF-B8 | Obj. 2 | Motor de Eventos | US-B8 | UC-B2, UC-B4, UC-B5, UC-B8 | — |
| RF-D1 | Obj. 3 | Coordenador de Turnaround | — | — | RNF-D1, RNF-D2, RNF-D4, RNF-D6 |
| RF-D2 | Obj. 2 e 3 | Coordenador de Turnaround | — | — | RNF-D1, RNF-D2, RNF-D6 |
| RF-D3 | Obj. 3 | Coordenador de Turnaround | — | — | RNF-D1, RNF-D2, RNF-D3, RNF-D6 |
| RF-D4 | Obj. 3 | Autoridade de Liberação | — | — | RNF-D1, RNF-D2, RNF-D5, RNF-D6 |
| RF-D5 | Obj. 3 | Coordenador de Turnaround | — | — | RNF-D1, RNF-D2, RNF-D5, RNF-D6 |
| RF-D6 | Obj. 1 | Coordenador de Turnaround | — | — | RNF-D1, RNF-D2, RNF-D3, RNF-D6 |
| RF-D7 | Obj. 1 e 3 | Coordenador de Turnaround | — | — | RNF-D1, RNF-D2, RNF-D6 |
| RF-D8 | Obj. 2 | Coordenador de Turnaround | — | — | RNF-D1, RNF-D2, RNF-D6 |
| RF-D9 | Obj. 3 | Operador de Solo/Rampa | — | — | RNF-D1, RNF-D2, RNF-D5, RNF-D6 |

### A.2 Objetivos × requisitos funcionais

| Objetivo | RFs que o atendem |
|---|---|
| Objetivo 1 | RF-B2, RF-B3, RF-B7, RF-D6, RF-D7 |
| Objetivo 2 | RF-B1, RF-B2, RF-B3, RF-B4, RF-B5, RF-B6, RF-B8, RF-D2, RF-D8 |
| Objetivo 3 | RF-B4, RF-B5, RF-D1, RF-D2, RF-D3, RF-D4, RF-D5, RF-D7, RF-D9 |

### A.3 Requisitos não funcionais × requisitos funcionais

| RNF | Característica ISO/IEC 25010 | RFs cobertos |
|---|---|---|
| RNF-B1 | Confiabilidade (disponibilidade) | RF-B1, RF-B2, RF-B3, RF-B4, RF-B5, RF-B6 |
| RNF-B2 | Confiabilidade (tolerância a falhas) | RF-B2, RF-B3, RF-B4, RF-B5, RF-B6 |
| RNF-B3 | Portabilidade (adaptabilidade) | — |
| RNF-B4 | Portabilidade (instalabilidade) | — |
| RNF-D1 | Confiabilidade (disponibilidade) | RF-D1, RF-D2, RF-D3, RF-D4, RF-D5, RF-D6, RF-D7, RF-D8, RF-D9 |
| RNF-D2 | Confiabilidade (recuperabilidade) | RF-D1, RF-D2, RF-D3, RF-D4, RF-D5, RF-D6, RF-D7, RF-D8, RF-D9 |
| RNF-D3 | Manutenibilidade (modificabilidade) | RF-D3, RF-D6 |
| RNF-D4 | Manutenibilidade (modificabilidade) | RF-B4, RF-D1 |
| RNF-D5 | Manutenibilidade (testabilidade) | RF-D4, RF-D5, RF-D9 |
| RNF-D6 | Manutenibilidade (analisabilidade) | RF-D1, RF-D2, RF-D3, RF-D4, RF-D5, RF-D6, RF-D7, RF-D8, RF-D9 |

### A.4 Lacunas encontradas

- RF-D1 sem estória (K.2)
- RF-D2 sem estória (K.2)
- RF-D3 sem estória (K.2)
- RF-D4 sem estória (K.2)
- RF-D5 sem estória (K.2)
- RF-D6 sem estória (K.2)
- RF-D7 sem estória (K.2)
- RF-D8 sem estória (K.2)
- RF-D9 sem estória (K.2)
- RF-D1 sem caso de uso (K.3)
- RF-D2 sem caso de uso (K.3)
- RF-D3 sem caso de uso (K.3)
- RF-D4 sem caso de uso (K.3)
- RF-D5 sem caso de uso (K.3)
- RF-D6 sem caso de uso (K.3)
- RF-D7 sem caso de uso (K.3)
- RF-D8 sem caso de uso (K.3)
- RF-D9 sem caso de uso (K.3)
- RNF-B3 sem RF associado
- RNF-B4 sem RF associado
<!-- matriz:fim -->
