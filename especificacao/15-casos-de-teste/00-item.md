# 15 CASOS DE TESTE

**PRODUTO:** Aircraft Turnaround Orchestration System

<!-- Item 15, tarefa-mãe T15 (issue #147), critérios C15.1 a C15.8. A introdução do item fica aqui; a planilha fica
em area-a.md a area-d.md, uma seção "## UCnn – <nome>" por caso de uso, e o gerador as põe em ordem de caso de uso.
Colunas da planilha (C15.1), lidas pelo script da matriz:
  | ID | Caso de uso | Cenário | Estória e critério de aceite | Caso de teste | Pré-condições | Dados de entrada | Passos | Resultado esperado |
O critério de aceite é escrito como USnnn-CAn, em que n é o número da linha do critério na estória (item 7); um caso
de teste pode citar mais de um, separados por vírgula. A planilha entra só no PDF (B4).
ID provisório por área durante a escrita, CT-A001, CT-B001, CT-C001 e CT-D001 em diante, cada área com a sua
sequência; na consolidação, um script renumera tudo para CT-001 em diante, na ordem do documento (ADR-0022), com
scripts/renumerar_casos_de_teste.py; scripts/conferir_casos_de_teste.py confere C15.1, C15.2, C15.3 e C15.5. -->

Os casos de teste verificam se o Aircraft Turnaround Orchestration System faz o que as estórias de usuário (item 7) e as especificações de caso de uso (item 10) descrevem. Eles estão numa planilha, uma tabela por caso de uso, na ordem dos casos de uso. Cada linha é um caso de teste que outra pessoa consegue executar sem conhecer quem o escreveu: diz de onde parte, com que dados, o que fazer e o que deve acontecer.

## 15.1 Colunas da planilha

| Coluna | O que contém |
|---|---|
| ID | Identificador único do caso de teste, CT-001 em diante, na ordem da planilha, como decidido no registro de decisão de arquitetura (ADR) 0022. |
| Caso de uso | O caso de uso do item 10 que o caso de teste percorre. |
| Cenário | Os passos dos fluxos percorridos: FP*n* é o passo *n* do fluxo básico, A*n*.*m* é o passo *m* do fluxo alternativo A*n*, e E*n*.*m*, o do fluxo de exceção E*n* (por exemplo, "FP1–FP3 / A1.1–A1.3"). |
| Estória e critério de aceite | O critério de aceite conferido, como USnnn-CAn, em que n é a linha do critério na estória; pode haver mais de um. |
| Caso de teste | O título, que diz o que é conferido. |
| Pré-condições | A situação antes do teste: usuários autenticados, turnarounds, registros já feitos e o horário do relógio. |
| Dados de entrada | Os valores informados, com data, hora e fuso, identificadores e quantidades reais, e não "dados válidos"; onde a regra tem limite, o valor do limite e o primeiro valor fora dele. |
| Passos | As ações numeradas, na ordem em que são feitas. |
| Resultado esperado | O que se observa ao final: a mensagem exibida, o estado resultante, o registro gravado ou o alerta emitido, coerente com o "ENTÃO" do critério de aceite. |

## 15.2 Massa de teste e ambiente

Cada área descreve, antes da planilha, a massa de teste que os seus casos usam: usuários, equipes, turnarounds, tarefas e registros, com os identificadores universais únicos (UUID) de cada um. Os casos de teste rodam num ambiente com relógio controlado. As telas mostram o horário local de Brasília, e o sistema grava em tempo universal coordenado (UTC), como manda a ADR-0016; cada área diz a data e o fuso que a sua massa usa. Os parâmetros configuráveis do requisito não funcional (RNF) 21, como as tolerâncias e os gatilhos dos alertas, têm o valor escrito na massa de cada área.

## 15.3 Cobertura e conferência

Todo critério de aceite das 44 estórias tem pelo menos um caso de teste, e todo caso de teste aponta para um critério que existe. Para cada um dos 37 casos de uso, o fluxo básico e cada fluxo alternativo e de exceção são percorridos por pelo menos um caso de teste. A relação entre critério de aceite e casos de teste está na matriz de rastreabilidade (Apêndice A, seção A.5; ADR-0021). As duas coberturas, as colunas, os IDs e a numeração dos passos são conferidos por script (`scripts/conferir_casos_de_teste.py`), e a matriz é gerada da própria planilha.

