# APÊNDICE A — MATRIZ DE RASTREABILIDADE

A matriz cruza os requisitos funcionais (item 6) com os objetivos (item 1), os atores (item 5), as estórias de usuário (item 7), os casos de uso (itens 9 e 10) e os requisitos não funcionais (item 8). Ela mostra que todo requisito funcional atende a um objetivo e tem estória e caso de uso, e que todo requisito não funcional se aplica a requisitos funcionais definidos (ADR-0012).

As tabelas abaixo são **geradas** pelo script `scripts/gerar_matriz_rastreabilidade.py` a partir dos arquivos de área. Não edite o trecho entre os marcadores: altere os requisitos, as estórias ou os casos de uso e rode o script de novo.

<!-- matriz:inicio -->
### A.1 Requisitos funcionais × objetivos, atores, estórias, casos de uso e RNFs

| RF | Objetivo | Ator / usuário | Estória | Caso(s) de uso | RNFs aplicáveis |
|---|---|---|---|---|---|
| RF-1 | Obj. 2 | Usuário | US001 | UC01 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-10, RNF-19, RNF-20 |
| RF-2 | Obj. 2 | Administrador do Sistema | US002 | UC02 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 |
| RF-3 | Obj. 1 e 2 | Coordenador de Turnaround | US003 | UC03 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 |
| RF-4 | Obj. 2 | Coordenador de Turnaround | US004 | UC04, UC05 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 |
| RF-5 | Obj. 1 e 2 | Coordenador de Turnaround | US005 | UC05, UC06 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 |
| RF-6 | Obj. 2 | Coordenador de Turnaround | US006 | UC06 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 |
| RF-7 | Obj. 2 | Coordenador de Turnaround | US007 | UC07 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 |
| RF-8 | Obj. 1 e 2 | Coordenador de Turnaround | US008 | UC05, UC08 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 |
| RF-9 | Obj. 2 | Administrador do Sistema | US009 | UC09 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 |
| RF-10 | Obj. 1 e 3 | Coordenador de Turnaround | US010 | UC10 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 |
| RF-11 | Obj. 1 e 2 | Coordenador de Turnaround | US011 | UC05, UC11 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 |
| RF-12 | Obj. 1 e 2 | Operador de Solo/Rampa | US012 | UC10, UC12 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-9, RNF-11, RNF-19, RNF-20 |
| RF-13 | Obj. 1 e 2 | Coordenador de Turnaround | US013 | UC12, UC13 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 |
| RF-14 | Obj. 2 | Operador de Solo/Rampa | US014 | UC14 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-9, RNF-10, RNF-11, RNF-20 |
| RF-15 | Obj. 1 e 2 | Operador de Solo/Rampa | US015 | UC15 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-8, RNF-9, RNF-20 |
| RF-16 | Obj. 1 e 2 | Operador de Solo/Rampa | US016 | UC16, UC19 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-8, RNF-9, RNF-20 |
| RF-17 | Obj. 2 e 3 | Operador de Solo/Rampa | US017 | UC17 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-8, RNF-9, RNF-20, RNF-22 |
| RF-18 | Obj. 2 e 3 | Operador de Solo/Rampa | US018 | UC18 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-8, RNF-9, RNF-20 |
| RF-19 | Obj. 2 | Operador de Solo/Rampa | US019 | UC16, UC19 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-8, RNF-9, RNF-20 |
| RF-20 | Obj. 1 | Motor de Eventos | US020 | UC18, UC20 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-19, RNF-20 |
| RF-21 | Obj. 2 | Motor de Eventos | US021 | UC15, UC17, UC18, UC21 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-11, RNF-19, RNF-20 |
| RF-22 | Obj. 1 e 3 | Motor de Eventos | US022 | UC24 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-19, RNF-20 |
| RF-23 | Obj. 1 e 3 | Motor de Eventos | US023 | UC23, UC24 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-19, RNF-20 |
| RF-24 | Obj. 3 | Motor de Eventos | US024 | UC23, UC24 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-16, RNF-17, RNF-19, RNF-20 |
| RF-25 | Obj. 2 e 3 | Coordenador de Turnaround | US025 | UC22 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-11, RNF-13, RNF-14, RNF-15, RNF-16, RNF-17, RNF-18, RNF-19, RNF-20, RNF-21 |
| RF-26 | Obj. 1 e 2 | Coordenador de Turnaround | US026 | UC23 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-11, RNF-13, RNF-14, RNF-15, RNF-16, RNF-17, RNF-18, RNF-19, RNF-20 |
| RF-27 | Obj. 2 e 3 | Motor de Eventos | US027 | UC25, UC31 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-15, RNF-19, RNF-20, RNF-21 |
| RF-28 | Obj. 3 | Motor de Eventos | US028 | UC25 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-15, RNF-19, RNF-20, RNF-21 |
| RF-29 | Obj. 3 | Motor de Eventos | US029 | UC24, UC25 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-15, RNF-19, RNF-20 |
| RF-30 | Obj. 3 | Motor de Eventos | US030 | UC25 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-15, RNF-19, RNF-20, RNF-21 |
| RF-31 | Obj. 3 | Motor de Eventos | US031 | UC25 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-15, RNF-19, RNF-20, RNF-21 |
| RF-32 | Obj. 2 | Motor de Eventos | US032 | UC27 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-13, RNF-19, RNF-20, RNF-21 |
| RF-33 | Obj. 3 | Coordenador de Turnaround | US033 | UC22, UC25, UC26, UC31 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-11, RNF-13, RNF-14, RNF-15, RNF-16, RNF-17, RNF-18, RNF-19, RNF-20 |
| RF-34 | Obj. 1 e 3 | Coordenador de Turnaround | US034 | UC28 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-13, RNF-14, RNF-18, RNF-19, RNF-20, RNF-21 |
| RF-35 | Obj. 2 | Coordenador de Turnaround | US035 | UC27 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-13, RNF-18, RNF-19, RNF-20 |
| RF-36 | Obj. 3 | Coordenador de Turnaround | US036 | UC29 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-22, RNF-24 |
| RF-37 | Obj. 2 e 3 | Coordenador de Turnaround | US037 | UC30 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-24 |
| RF-38 | Obj. 3 | Coordenador de Turnaround | US038 | UC31 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-15, RNF-18, RNF-19, RNF-20, RNF-21, RNF-24 |
| RF-39 | Obj. 3 | Autoridade de Liberação | US039 | UC32 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-23, RNF-24 |
| RF-40 | Obj. 3 | Coordenador de Turnaround | US040 | UC33 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-23, RNF-24 |
| RF-41 | Obj. 1 | Coordenador de Turnaround | US041 | UC34 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-21, RNF-24 |
| RF-42 | Obj. 1 e 3 | Coordenador de Turnaround | US042 | UC35 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-24 |
| RF-43 | Obj. 2 | Coordenador de Turnaround | US043 | UC36 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-24 |
| RF-44 | Obj. 3 | Operador de Solo/Rampa | US044 | UC37 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-9, RNF-19, RNF-20, RNF-23, RNF-24 |

### A.2 Objetivos × requisitos funcionais

| Objetivo | RFs que o atendem |
|---|---|
| Objetivo 1 | RF-3, RF-5, RF-8, RF-10, RF-11, RF-12, RF-13, RF-15, RF-16, RF-20, RF-22, RF-23, RF-26, RF-34, RF-41, RF-42 |
| Objetivo 2 | RF-1, RF-2, RF-3, RF-4, RF-5, RF-6, RF-7, RF-8, RF-9, RF-11, RF-12, RF-13, RF-14, RF-15, RF-16, RF-17, RF-18, RF-19, RF-21, RF-25, RF-26, RF-27, RF-32, RF-35, RF-37, RF-43 |
| Objetivo 3 | RF-10, RF-17, RF-18, RF-22, RF-23, RF-24, RF-25, RF-27, RF-28, RF-29, RF-30, RF-31, RF-33, RF-34, RF-36, RF-37, RF-38, RF-39, RF-40, RF-42, RF-44 |

### A.3 Requisitos não funcionais × requisitos funcionais

| RNF | Característica ISO/IEC 25010 | RFs cobertos |
|---|---|---|
| RNF-1 | Segurança (confidencialidade e integridade) | todos os RFs |
| RNF-2 | Segurança (responsabilização e integridade) | todos os RFs |
| RNF-3 | Segurança (confidencialidade e autenticidade) | todos os RFs |
| RNF-4 | Compatibilidade (interoperabilidade) | RF-2, RF-3, RF-4, RF-5, RF-6, RF-7, RF-8, RF-9, RF-10, RF-11, RF-12, RF-13 |
| RNF-5 | Segurança (autenticidade e confidencialidade) | todos os RFs |
| RNF-6 | Segurança (confidencialidade e responsabilização) | todos os RFs |
| RNF-7 | Confiabilidade (disponibilidade) | RF-14, RF-15, RF-16, RF-17, RF-18, RF-19 |
| RNF-8 | Confiabilidade (tolerância a falhas) | RF-15, RF-16, RF-17, RF-18, RF-19 |
| RNF-9 | Portabilidade (adaptabilidade) | RF-12, RF-14, RF-15, RF-16, RF-17, RF-18, RF-19, RF-44 |
| RNF-10 | Portabilidade (instalabilidade) | RF-1, RF-14 |
| RNF-11 | Eficiência de desempenho (comportamento no tempo) | RF-12, RF-14, RF-21, RF-25, RF-26, RF-33 |
| RNF-12 | Eficiência de desempenho (comportamento no tempo) | RF-22, RF-23, RF-24, RF-27, RF-28, RF-29, RF-30, RF-31 |
| RNF-13 | Eficiência de desempenho (capacidade) | RF-22, RF-23, RF-24, RF-25, RF-26, RF-27, RF-28, RF-29, RF-30, RF-31, RF-32, RF-33, RF-34, RF-35 |
| RNF-14 | Eficiência de desempenho (comportamento no tempo) | RF-25, RF-26, RF-33, RF-34 |
| RNF-15 | Usabilidade (operabilidade) | RF-25, RF-26, RF-27, RF-28, RF-29, RF-30, RF-31, RF-33, RF-38 |
| RNF-16 | Usabilidade (apreensibilidade) | RF-24, RF-25, RF-26, RF-33 |
| RNF-17 | Usabilidade (acessibilidade) | RF-24, RF-25, RF-26, RF-33 |
| RNF-18 | Usabilidade (operabilidade) | RF-2, RF-3, RF-4, RF-5, RF-6, RF-7, RF-8, RF-9, RF-10, RF-11, RF-13, RF-25, RF-26, RF-33, RF-34, RF-35, RF-36, RF-37, RF-38, RF-39, RF-40, RF-41, RF-42, RF-43 |
| RNF-19 | Confiabilidade (disponibilidade) | RF-1, RF-2, RF-3, RF-4, RF-5, RF-6, RF-7, RF-8, RF-9, RF-10, RF-11, RF-12, RF-13, RF-20, RF-21, RF-22, RF-23, RF-24, RF-25, RF-26, RF-27, RF-28, RF-29, RF-30, RF-31, RF-32, RF-33, RF-34, RF-35, RF-36, RF-37, RF-38, RF-39, RF-40, RF-41, RF-42, RF-43, RF-44 |
| RNF-20 | Confiabilidade (recuperabilidade) | todos os RFs |
| RNF-21 | Manutenibilidade (modificabilidade) | RF-25, RF-27, RF-28, RF-30, RF-31, RF-32, RF-34, RF-38, RF-41 |
| RNF-22 | Manutenibilidade (modificabilidade) | RF-17, RF-36 |
| RNF-23 | Manutenibilidade (testabilidade) | RF-39, RF-40, RF-44 |
| RNF-24 | Manutenibilidade (analisabilidade) | RF-36, RF-37, RF-38, RF-39, RF-40, RF-41, RF-42, RF-43, RF-44 |

### A.4 Lacunas encontradas

- Nenhuma.
<!-- matriz:fim -->
