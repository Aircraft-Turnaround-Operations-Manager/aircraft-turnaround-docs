# APÊNDICE A — MATRIZ DE RASTREABILIDADE

A matriz cruza os requisitos funcionais (item 6) com os objetivos (item 1), os atores (item 5), as estórias de usuário (item 7), os casos de uso (itens 9 e 10) e os requisitos não funcionais (item 8). Ela mostra que todo requisito funcional atende a um objetivo e tem estória e caso de uso, e que todo requisito não funcional se aplica a requisitos funcionais definidos (ADR-0012).

As tabelas abaixo são **geradas** pelo script `scripts/gerar_matriz_rastreabilidade.py` a partir dos arquivos de área. Não edite o trecho entre os marcadores: altere os requisitos, as estórias ou os casos de uso e rode o script de novo.

<!-- matriz:inicio -->
### A.1 Requisitos funcionais × objetivos, atores, estórias, casos de uso e RNFs

| RF | Objetivo | Ator / usuário | Estória | Caso(s) de uso | RNFs aplicáveis |
|---|---|---|---|---|---|
| RF-A1 | Obj. 2 | Usuário | US-A1 | UC-A1 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6 |
| RF-A2 | Obj. 2 | Administrador do Sistema | US-A2 | UC-A2 | RNF-A1, RNF-A2, RNF-A3, RNF-A4, RNF-A5, RNF-A6 |
| RF-A3 | Obj. 1 e 2 | Coordenador de Turnaround | US-A3 | UC-A3 | RNF-A1, RNF-A2, RNF-A3, RNF-A4, RNF-A5, RNF-A6 |
| RF-A4 | Obj. 2 | Coordenador de Turnaround | US-A4 | UC-A4, UC-A5 | RNF-A1, RNF-A2, RNF-A3, RNF-A4, RNF-A5, RNF-A6 |
| RF-A5 | Obj. 1 e 2 | Coordenador de Turnaround | US-A5 | UC-A5, UC-A6 | RNF-A1, RNF-A2, RNF-A3, RNF-A4, RNF-A5, RNF-A6 |
| RF-A6 | Obj. 2 | Coordenador de Turnaround | US-A6 | UC-A6 | RNF-A1, RNF-A2, RNF-A3, RNF-A4, RNF-A5, RNF-A6 |
| RF-A7 | Obj. 2 | Coordenador de Turnaround | US-A7 | UC-A7 | RNF-A1, RNF-A2, RNF-A3, RNF-A4, RNF-A5, RNF-A6 |
| RF-A8 | Obj. 1 e 2 | Coordenador de Turnaround | US-A8 | UC-A5, UC-A8 | RNF-A1, RNF-A2, RNF-A3, RNF-A4, RNF-A5, RNF-A6 |
| RF-A9 | Obj. 2 | Administrador do Sistema | US-A9 | UC-A9 | RNF-A1, RNF-A2, RNF-A3, RNF-A4, RNF-A5, RNF-A6 |
| RF-A10 | Obj. 1 e 3 | Coordenador de Turnaround | US-A10 | UC-A10 | RNF-A1, RNF-A2, RNF-A3, RNF-A4, RNF-A5, RNF-A6 |
| RF-A11 | Obj. 1 e 2 | Coordenador de Turnaround | US-A11 | UC-A5, UC-A11 | RNF-A1, RNF-A2, RNF-A3, RNF-A4, RNF-A5, RNF-A6 |
| RF-A12 | Obj. 1 e 2 | Operador de Solo/Rampa | US-A12 | UC-A10, UC-A12 | RNF-A1, RNF-A2, RNF-A3, RNF-A4, RNF-A5, RNF-A6 |
| RF-A13 | Obj. 1 e 2 | Coordenador de Turnaround | US-A13 | UC-A12, UC-A13 | RNF-A1, RNF-A2, RNF-A3, RNF-A4, RNF-A5, RNF-A6 |
| RF-B1 | Obj. 2 | Operador de Solo/Rampa | US-B1 | UC-B1, UC-B8 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-B1, RNF-C1 |
| RF-B2 | Obj. 1 e 2 | Operador de Solo/Rampa | US-B2 | UC-B2, UC-B8 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-B1, RNF-B2 |
| RF-B3 | Obj. 1 e 2 | Operador de Solo/Rampa | US-B3 | UC-B3, UC-B6, UC-B8 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-B1, RNF-B2 |
| RF-B4 | Obj. 2 e 3 | Operador de Solo/Rampa | US-B4 | UC-B4, UC-B8 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-B1, RNF-B2, RNF-D4 |
| RF-B5 | Obj. 2 e 3 | Operador de Solo/Rampa | US-B5 | UC-B5, UC-B8 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-B1, RNF-B2 |
| RF-B6 | Obj. 2 | Operador de Solo/Rampa | US-B6 | UC-B3, UC-B6, UC-B8 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-B1, RNF-B2 |
| RF-B7 | Obj. 1 | Motor de Eventos | US-B7 | UC-B5, UC-B7, UC-B8 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6 |
| RF-B8 | Obj. 2 | Motor de Eventos | US-B8 | UC-B2, UC-B4, UC-B5, UC-B8 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-C1 |
| RF-C1 | Obj. 1 e 3 | Motor de Eventos | US-C1 | UC-C3 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-C2, RNF-C3 |
| RF-C2 | Obj. 1 e 3 | Motor de Eventos | US-C2 | UC-C2, UC-C3 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-C2, RNF-C3 |
| RF-C3 | Obj. 3 | Motor de Eventos | US-C3 | UC-C2, UC-C3 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-C2, RNF-C3, RNF-C6, RNF-C7 |
| RF-C4 | Obj. 2 e 3 | Coordenador de Turnaround | US-C4 | UC-C1 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-C1, RNF-C3, RNF-C4, RNF-C5, RNF-C6, RNF-C7, RNF-C8 |
| RF-C5 | Obj. 1 e 2 | Coordenador de Turnaround | US-C5 | UC-C2 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-C1, RNF-C3, RNF-C4, RNF-C5, RNF-C6, RNF-C7, RNF-C8 |
| RF-C6 | Obj. 2 e 3 | Motor de Eventos | US-C6 | UC-C4 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-C2, RNF-C3, RNF-C5 |
| RF-C7 | Obj. 3 | Motor de Eventos | US-C7 | UC-C4 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-C2, RNF-C3, RNF-C5 |
| RF-C8 | Obj. 3 | Motor de Eventos | US-C8 | UC-C3, UC-C4 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-C2, RNF-C3, RNF-C5 |
| RF-C9 | Obj. 3 | Motor de Eventos | US-C9 | UC-C4 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-C2, RNF-C3, RNF-C5 |
| RF-C10 | Obj. 3 | Motor de Eventos | US-C10 | UC-C4 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-C2, RNF-C3, RNF-C5 |
| RF-C11 | Obj. 2 | Motor de Eventos | US-C11 | UC-C6 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-C3 |
| RF-C12 | Obj. 3 | Coordenador de Turnaround | US-C12 | UC-C1, UC-C4, UC-C5 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-C1, RNF-C3, RNF-C4, RNF-C5, RNF-C6, RNF-C7, RNF-C8 |
| RF-C13 | Obj. 1 e 3 | Coordenador de Turnaround | US-C13 | UC-C7 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-C3, RNF-C4, RNF-C8 |
| RF-C14 | Obj. 2 | Coordenador de Turnaround | US-C14 | UC-C6 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-C3 |
| RF-D1 | Obj. 3 | Coordenador de Turnaround | US-D1 | UC-D1 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-D1, RNF-D2, RNF-D4, RNF-D6 |
| RF-D2 | Obj. 2 e 3 | Coordenador de Turnaround | US-D2 | UC-D2 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-D1, RNF-D2, RNF-D6 |
| RF-D3 | Obj. 3 | Coordenador de Turnaround | US-D3 | UC-D3 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-C5, RNF-D1, RNF-D2, RNF-D3, RNF-D6 |
| RF-D4 | Obj. 3 | Autoridade de Liberação | US-D4 | UC-D4 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-D1, RNF-D2, RNF-D5, RNF-D6 |
| RF-D5 | Obj. 3 | Coordenador de Turnaround | US-D5 | UC-D5 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-D1, RNF-D2, RNF-D5, RNF-D6 |
| RF-D6 | Obj. 1 | Coordenador de Turnaround | US-D6 | UC-D6 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-D1, RNF-D2, RNF-D3, RNF-D6 |
| RF-D7 | Obj. 1 e 3 | Coordenador de Turnaround | US-D7 | UC-D7 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-D1, RNF-D2, RNF-D6 |
| RF-D8 | Obj. 2 | Coordenador de Turnaround | US-D8 | UC-D8 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-D1, RNF-D2, RNF-D6 |
| RF-D9 | Obj. 3 | Operador de Solo/Rampa | US-D9 | UC-D9 | RNF-A1, RNF-A2, RNF-A3, RNF-A5, RNF-A6, RNF-D1, RNF-D2, RNF-D5, RNF-D6 |

### A.2 Objetivos × requisitos funcionais

| Objetivo | RFs que o atendem |
|---|---|
| Objetivo 1 | RF-A3, RF-A5, RF-A8, RF-A10, RF-A11, RF-A12, RF-A13, RF-B2, RF-B3, RF-B7, RF-C1, RF-C2, RF-C5, RF-C13, RF-D6, RF-D7 |
| Objetivo 2 | RF-A1, RF-A2, RF-A3, RF-A4, RF-A5, RF-A6, RF-A7, RF-A8, RF-A9, RF-A11, RF-A12, RF-A13, RF-B1, RF-B2, RF-B3, RF-B4, RF-B5, RF-B6, RF-B8, RF-C4, RF-C5, RF-C6, RF-C11, RF-C14, RF-D2, RF-D8 |
| Objetivo 3 | RF-A10, RF-B4, RF-B5, RF-C1, RF-C2, RF-C3, RF-C4, RF-C6, RF-C7, RF-C8, RF-C9, RF-C10, RF-C12, RF-C13, RF-D1, RF-D2, RF-D3, RF-D4, RF-D5, RF-D7, RF-D9 |

### A.3 Requisitos não funcionais × requisitos funcionais

| RNF | Característica ISO/IEC 25010 | RFs cobertos |
|---|---|---|
| RNF-A1 | Segurança (confidencialidade e integridade) | todos os RFs |
| RNF-A2 | Segurança (responsabilização e integridade) | todos os RFs |
| RNF-A3 | Segurança (confidencialidade e autenticidade) | todos os RFs |
| RNF-A4 | Compatibilidade (interoperabilidade) | RF-A2, RF-A3, RF-A4, RF-A5, RF-A6, RF-A7, RF-A8, RF-A9, RF-A10, RF-A11, RF-A12, RF-A13 |
| RNF-A5 | Segurança (autenticidade e confidencialidade) | todos os RFs |
| RNF-A6 | Segurança (confidencialidade e responsabilização) | todos os RFs |
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

- RNF-B3 sem RF associado
- RNF-B4 sem RF associado
<!-- matriz:fim -->
