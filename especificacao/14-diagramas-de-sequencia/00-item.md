# 14 DIAGRAMAS DE SEQUÊNCIA

**PRODUTO:** Aircraft Turnaround Orchestration System

<!-- Item 14, tarefa-mãe T14 (issue #146), critérios C14.1 a C14.8. A introdução do item fica aqui; os diagramas
ficam em area-a.md a area-d.md, e o gerador (scripts/gerar_docx.py) os põe em ordem de caso de uso.
Formato de cada caso de uso nos arquivos de área, lido pelo script da matriz: o título "## UCnn – <nome do caso de
uso, igual ao item 10>", seguido da figura ../diagramas/14-sequencia-ucnn.png, cujo texto alternativo é a legenda
"Diagrama de Sequência do UCnn – <mesmo nome>" (C14.1).
Um diagrama grande pode ser dividido em partes, cada uma com a mesma legenda seguida de "(parte n: ...)".
Uma seção "## ..." sem UC no título (por exemplo, participantes e convenções da área) fica antes do primeiro caso
de uso que vem depois dela no arquivo. A fonte editável e a .svg têm o mesmo nome da .png (Y.6, Y.7); a ferramenta
sai da tarefa T02 (issue #141, decisão B3). scripts/conferir_sequencia.py confere C14.1, C14.4 e os arquivos do C14.8. -->

Os diagramas de sequência mostram, para cada caso de uso do item 10, a troca de mensagens entre o ator e as camadas do Aircraft Turnaround Orchestration System, na ordem dos passos do caso de uso. Há um diagrama por caso de uso, e o diagrama grande é dividido em partes. Os diagramas usam a linguagem de modelagem unificada (UML) e são desenhados em PlantUML, com a fonte editável ao lado da figura.

## 14.1 Notação

- **Ator e linhas de vida.** O ator que inicia a sequência é o do caso de uso (item 9), inclusive o Motor de Eventos nos casos de uso dele. Cada participante é uma classe do item 13, com a linha de vida tracejada e o estereótipo da camada: tela («boundary»), controle («control» e, nos painéis, «resolver»), serviço («service»), classe de negócio («entity»), repositório («repository») e o banco do serviço.
- **Mensagens.** A chamada é uma seta contínua com o método do item 13 e os argumentos; o retorno é uma seta tracejada. Cada acesso ao banco cita a tabela do item 12. As ativações mostram quanto tempo cada participante fica trabalhando.
- **Fragmentos.** `alt` (alternativas) e `opt` (opcional) têm a condição de guarda entre colchetes e o nome do fluxo do item 10 que representam (A*n* ou E*n*); `loop` repete; `ref` remete a outro caso de uso ou a um trecho já desenhado. `«include»` aparece como `ref` ao caso de uso incluído, e `«extend»`, como `opt` com a condição de extensão.
- **Fluxos agrupados.** Um fluxo que não muda a interação (por exemplo, o que só volta a um passo) pode ficar junto de outro ou numa nota; o arquivo de cada área diz quais foram agrupados.

## 14.2 Comunicação entre os serviços

Os quatro serviços do registro de decisão de arquitetura (ADR) 0015 conversam de dois jeitos. O pedido, quando um serviço precisa da decisão do dono do dado, é uma chamada direta com resposta. O aviso, quando algo já aconteceu, passa pela mensageria (RabbitMQ), com o envelope comum da ADR-0016. Nenhum serviço lê o banco de outro. Toda ação feita no site passa pela porta de entrada, que confere a sessão e o perfil a cada ação, como pede o requisito não funcional (RNF) 1; o fragmento `ref` "Verificar acesso na porta de entrada" resume essa conferência (ADR-0023). O Motor de Eventos não é uma classe: é o comportamento automático de serviços da Execução em Solo e do Monitoramento (item 13, seção 13.1), acionado por um registro, por um aviso ou pelo relógio.

## 14.3 Conferência

`scripts/conferir_sequencia.py` confere a legenda de cada figura contra o nome do item 10, os fluxos alternativos e de exceção de cada caso de uso, e a existência da figura, da imagem vetorial e da fonte. `scripts/conferir_classes.py --sequencia` confere que todo método chamado existe na classe do item 13 que recebe a mensagem, e a matriz de rastreabilidade (Apêndice A, seção A.4) liga cada caso de uso aos seus diagramas.

