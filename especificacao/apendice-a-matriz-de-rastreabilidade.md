# APÊNDICE A — MATRIZ DE RASTREABILIDADE

A matriz cruza os requisitos funcionais (item 6) com os objetivos (item 1), os atores (item 5), as estórias de usuário (item 7), os casos de uso (itens 9 e 10) e os requisitos não funcionais (item 8). Ela mostra que todo requisito funcional atende a um objetivo e tem estória e caso de uso, e que todo requisito não funcional se aplica a requisitos funcionais definidos (ADR-0012).

As tabelas abaixo são **geradas** pelo script `scripts/gerar_matriz_rastreabilidade.py` a partir dos arquivos de área. Não edite o trecho entre os marcadores: altere os requisitos, as estórias ou os casos de uso e rode o script de novo.

<!-- matriz:inicio -->
### A.1 Requisitos funcionais × objetivos, atores, estórias, casos de uso e RNFs

| RF | Objetivo | Ator / usuário | Estória | Caso(s) de uso | RNFs aplicáveis |
|---|---|---|---|---|---|
| RF-A1 | Obj. 2 | Usuário | — | — | — |
| RF-A2 | Obj. 2 | Administrador do Sistema | — | — | — |
| RF-A3 | Obj. 1 e 2 | Coordenador de Turnaround | — | — | — |
| RF-A4 | Obj. 2 | Coordenador de Turnaround | — | — | — |
| RF-A5 | Obj. 1 e 2 | Coordenador de Turnaround | — | — | — |
| RF-A6 | Obj. 2 | Coordenador de Turnaround | — | — | — |
| RF-A7 | Obj. 2 | Coordenador de Turnaround | — | — | — |
| RF-A8 | Obj. 1 e 2 | Coordenador de Turnaround | — | — | — |
| RF-A9 | Obj. 2 | Administrador do Sistema | — | — | — |
| RF-A10 | Obj. 1 e 3 | Coordenador de Turnaround | — | — | — |
| RF-A11 | Obj. 1 e 2 | Coordenador de Turnaround | — | — | — |
| RF-A12 | Obj. 1 e 2 | Operador de Solo/Rampa | — | — | — |
| RF-A13 | Obj. 1 e 2 | Coordenador de Turnaround | — | — | — |
| RF-B1 | Obj. 2 | Operador de Solo/Rampa | US-B1 | UC-B1, UC-B8 | RNF-B1, RNF-C1 |
| RF-B2 | Obj. 1 e 2 | Operador de Solo/Rampa | US-B2 | UC-B2, UC-B8 | RNF-B1, RNF-B2 |
| RF-B3 | Obj. 1 e 2 | Operador de Solo/Rampa | US-B3 | UC-B3, UC-B6, UC-B8 | RNF-B1, RNF-B2 |
| RF-B4 | Obj. 2 e 3 | Operador de Solo/Rampa | US-B4 | UC-B4, UC-B8 | RNF-B1, RNF-B2, RNF-D4 |
| RF-B5 | Obj. 2 e 3 | Operador de Solo/Rampa | US-B5 | UC-B5, UC-B8 | RNF-B1, RNF-B2 |
| RF-B6 | Obj. 2 | Operador de Solo/Rampa | US-B6 | UC-B3, UC-B6, UC-B8 | RNF-B1, RNF-B2 |
| RF-B7 | Obj. 1 | Motor de Eventos | US-B7 | UC-B5, UC-B7, UC-B8 | — |
| RF-B8 | Obj. 2 | Motor de Eventos | US-B8 | UC-B2, UC-B4, UC-B5, UC-B8 | RNF-C1 |
| RF-C1 | Obj. 1 e 3 | Motor de Eventos | — | — | RNF-C2, RNF-C3 |
| RF-C2 | Obj. 1 e 3 | Motor de Eventos | — | — | RNF-C2, RNF-C3 |
| RF-C3 | Obj. 3 | Motor de Eventos | — | — | RNF-C2, RNF-C3, RNF-C6, RNF-C7 |
| RF-C4 | Obj. 2 e 3 | Coordenador de Turnaround | — | — | RNF-C1, RNF-C3, RNF-C4, RNF-C5, RNF-C6, RNF-C7, RNF-C8 |
| RF-C5 | Obj. 1 e 2 | Coordenador de Turnaround | — | — | RNF-C1, RNF-C3, RNF-C4, RNF-C5, RNF-C6, RNF-C7, RNF-C8 |
| RF-C6 | Obj. 2 e 3 | Motor de Eventos | — | — | RNF-C2, RNF-C3, RNF-C5 |
| RF-C7 | Obj. 3 | Motor de Eventos | — | — | RNF-C2, RNF-C3, RNF-C5 |
| RF-C8 | Obj. 3 | Motor de Eventos | — | — | RNF-C2, RNF-C3, RNF-C5 |
| RF-C9 | Obj. 3 | Motor de Eventos | — | — | RNF-C2, RNF-C3, RNF-C5 |
| RF-C10 | Obj. 3 | Motor de Eventos | — | — | RNF-C2, RNF-C3, RNF-C5 |
| RF-C11 | Obj. 2 | Motor de Eventos | — | — | RNF-C3 |
| RF-C12 | Obj. 3 | Coordenador de Turnaround | — | — | RNF-C1, RNF-C3, RNF-C4, RNF-C5, RNF-C6, RNF-C7, RNF-C8 |
| RF-C13 | Obj. 1 e 3 | Coordenador de Turnaround | — | — | RNF-C3, RNF-C4, RNF-C8 |
| RF-C14 | Obj. 2 | Coordenador de Turnaround | — | — | RNF-C3 |
| RF-D1 | Obj. 3 | Coordenador de Turnaround | US-D1 | UC-D1 | RNF-D1, RNF-D2, RNF-D4, RNF-D6 |
| RF-D2 | Obj. 2 e 3 | Coordenador de Turnaround | US-D2 | UC-D2 | RNF-D1, RNF-D2, RNF-D6 |
| RF-D3 | Obj. 3 | Coordenador de Turnaround | US-D3 | UC-D3 | RNF-C5, RNF-D1, RNF-D2, RNF-D3, RNF-D6 |
| RF-D4 | Obj. 3 | Autoridade de Liberação | US-D4 | UC-D4 | RNF-D1, RNF-D2, RNF-D5, RNF-D6 |
| RF-D5 | Obj. 3 | Coordenador de Turnaround | US-D5 | UC-D5 | RNF-D1, RNF-D2, RNF-D5, RNF-D6 |
| RF-D6 | Obj. 1 | Coordenador de Turnaround | US-D6 | UC-D6 | RNF-D1, RNF-D2, RNF-D3, RNF-D6 |
| RF-D7 | Obj. 1 e 3 | Coordenador de Turnaround | US-D7 | UC-D7 | RNF-D1, RNF-D2, RNF-D6 |
| RF-D8 | Obj. 2 | Coordenador de Turnaround | US-D8 | UC-D8 | RNF-D1, RNF-D2, RNF-D6 |
| RF-D9 | Obj. 3 | Operador de Solo/Rampa | US-D9 | UC-D9 | RNF-D1, RNF-D2, RNF-D5, RNF-D6 |

### A.2 Objetivos × requisitos funcionais

| Objetivo | RFs que o atendem |
|---|---|
| Objetivo 1 | RF-A3, RF-A5, RF-A8, RF-A10, RF-A11, RF-A12, RF-A13, RF-B2, RF-B3, RF-B7, RF-C1, RF-C2, RF-C5, RF-C13, RF-D6, RF-D7 |
| Objetivo 2 | RF-A1, RF-A2, RF-A3, RF-A4, RF-A5, RF-A6, RF-A7, RF-A8, RF-A9, RF-A11, RF-A12, RF-A13, RF-B1, RF-B2, RF-B3, RF-B4, RF-B5, RF-B6, RF-B8, RF-C4, RF-C5, RF-C6, RF-C11, RF-C14, RF-D2, RF-D8 |
| Objetivo 3 | RF-A10, RF-B4, RF-B5, RF-C1, RF-C2, RF-C3, RF-C4, RF-C6, RF-C7, RF-C8, RF-C9, RF-C10, RF-C12, RF-C13, RF-D1, RF-D2, RF-D3, RF-D4, RF-D5, RF-D7, RF-D9 |

### A.3 Requisitos não funcionais × requisitos funcionais

| RNF | Característica ISO/IEC 25010 | RFs cobertos |
|---|---|---|
| RNF-B1 | Confiabilidade (disponibilidade) | RF-B1, RF-B2, RF-B3, RF-B4, RF-B5, RF-B6 |
| RNF-B2 | Confiabilidade (tolerância a falhas) | RF-B2, RF-B3, RF-B4, RF-B5, RF-B6 |
| RNF-B3 | Portabilidade (adaptabilidade) | — |
| RNF-B4 | Portabilidade (instalabilidade) | — |
| RNF-C1 | Eficiência de desempenho (comportamento no tempo) | RF-B1, RF-B8, RF-C4, RF-C5, RF-C12 |
| RNF-C2 | Eficiência de desempenho (comportamento no tempo) | RF-C1, RF-C2, RF-C3, RF-C6, RF-C7, RF-C8, RF-C9, RF-C10 |
| RNF-C3 | Eficiência de desempenho (capacidade) | RF-C1, RF-C2, RF-C3, RF-C4, RF-C5, RF-C6, RF-C7, RF-C8, RF-C9, RF-C10, RF-C11, RF-C12, RF-C13, RF-C14 |
| RNF-C4 | Eficiência de desempenho (comportamento no tempo) | RF-C4, RF-C5, RF-C12, RF-C13 |
| RNF-C5 | Usabilidade (operabilidade) | RF-C4, RF-C5, RF-C6, RF-C7, RF-C8, RF-C9, RF-C10, RF-C12, RF-D3 |
| RNF-C6 | Usabilidade (apreensibilidade) | RF-C3, RF-C4, RF-C5, RF-C12 |
| RNF-C7 | Usabilidade (acessibilidade) | RF-C3, RF-C4, RF-C5, RF-C12 |
| RNF-C8 | Usabilidade (operabilidade) | RF-C4, RF-C5, RF-C12, RF-C13 |
| RNF-D1 | Confiabilidade (disponibilidade) | RF-D1, RF-D2, RF-D3, RF-D4, RF-D5, RF-D6, RF-D7, RF-D8, RF-D9 |
| RNF-D2 | Confiabilidade (recuperabilidade) | RF-D1, RF-D2, RF-D3, RF-D4, RF-D5, RF-D6, RF-D7, RF-D8, RF-D9 |
| RNF-D3 | Manutenibilidade (modificabilidade) | RF-D3, RF-D6 |
| RNF-D4 | Manutenibilidade (modificabilidade) | RF-B4, RF-D1 |
| RNF-D5 | Manutenibilidade (testabilidade) | RF-D4, RF-D5, RF-D9 |
| RNF-D6 | Manutenibilidade (analisabilidade) | RF-D1, RF-D2, RF-D3, RF-D4, RF-D5, RF-D6, RF-D7, RF-D8, RF-D9 |

### A.4 Lacunas encontradas

- RF-A1 sem estória (K.2)
- RF-A2 sem estória (K.2)
- RF-A3 sem estória (K.2)
- RF-A4 sem estória (K.2)
- RF-A5 sem estória (K.2)
- RF-A6 sem estória (K.2)
- RF-A7 sem estória (K.2)
- RF-A8 sem estória (K.2)
- RF-A9 sem estória (K.2)
- RF-A10 sem estória (K.2)
- RF-A11 sem estória (K.2)
- RF-A12 sem estória (K.2)
- RF-A13 sem estória (K.2)
- RF-C1 sem estória (K.2)
- RF-C2 sem estória (K.2)
- RF-C3 sem estória (K.2)
- RF-C4 sem estória (K.2)
- RF-C5 sem estória (K.2)
- RF-C6 sem estória (K.2)
- RF-C7 sem estória (K.2)
- RF-C8 sem estória (K.2)
- RF-C9 sem estória (K.2)
- RF-C10 sem estória (K.2)
- RF-C11 sem estória (K.2)
- RF-C12 sem estória (K.2)
- RF-C13 sem estória (K.2)
- RF-C14 sem estória (K.2)
- RF-A1 sem caso de uso (K.3)
- RF-A2 sem caso de uso (K.3)
- RF-A3 sem caso de uso (K.3)
- RF-A4 sem caso de uso (K.3)
- RF-A5 sem caso de uso (K.3)
- RF-A6 sem caso de uso (K.3)
- RF-A7 sem caso de uso (K.3)
- RF-A8 sem caso de uso (K.3)
- RF-A9 sem caso de uso (K.3)
- RF-A10 sem caso de uso (K.3)
- RF-A11 sem caso de uso (K.3)
- RF-A12 sem caso de uso (K.3)
- RF-A13 sem caso de uso (K.3)
- RF-C1 sem caso de uso (K.3)
- RF-C2 sem caso de uso (K.3)
- RF-C3 sem caso de uso (K.3)
- RF-C4 sem caso de uso (K.3)
- RF-C5 sem caso de uso (K.3)
- RF-C6 sem caso de uso (K.3)
- RF-C7 sem caso de uso (K.3)
- RF-C8 sem caso de uso (K.3)
- RF-C9 sem caso de uso (K.3)
- RF-C10 sem caso de uso (K.3)
- RF-C11 sem caso de uso (K.3)
- RF-C12 sem caso de uso (K.3)
- RF-C13 sem caso de uso (K.3)
- RF-C14 sem caso de uso (K.3)
- RNF-B3 sem RF associado
- RNF-B4 sem RF associado
<!-- matriz:fim -->
