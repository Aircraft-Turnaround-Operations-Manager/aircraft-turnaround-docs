| # | REQUISITO NÃO-FUNCIONAL | NORMA ISO/IEC 25010 |
|---|---|---|
| RNF-B1 | As funções usadas pelo Operador de Solo/Rampa (consultar tarefas, registrar a execução, registrar desvio e confirmar por QR Code) devem estar disponíveis em pelo menos 99,5% do tempo de cada mês, 24 horas por dia, medido por verificação automática a cada 1 minuto; o tempo de indisponibilidade inclui paradas programadas. | Confiabilidade (disponibilidade) |
| RNF-B2 | Sem conexão com a internet, o sistema, no celular do Operador de Solo/Rampa, deve aceitar os registros de execução, de desvio e as leituras de QR Code por até 30 minutos, guardando o horário de cada ação no próprio aparelho com precisão de minuto completo, e enviá-los ao servidor em até 5 segundos depois que a conexão voltar, na ordem em que foram feitos. No teste com 50 registros feitos sem conexão, 100% devem chegar ao servidor, sem duplicação e com o horário da ação, e não o do envio. | Confiabilidade (tolerância a falhas) |
| RNF-B3 | As telas do Operador de Solo/Rampa devem funcionar, incluindo a leitura de QR Code pela câmera, nas duas versões mais recentes do Chrome no Android 10 ou superior e do Safari no iOS 16 ou superior, em telas de 360 a 430 pixels de largura, sem rolagem horizontal e sem texto ou botão cortado, conferido em um roteiro de teste executado em cada combinação. | Portabilidade (adaptabilidade) |
| RNF-B4 | O Operador de Solo/Rampa deve acessar o sistema pelo navegador do celular, por endereço web, sem instalar aplicativo de loja; do primeiro acesso de um usuário já cadastrado até a lista de tarefas, o caminho deve ter no máximo 3 telas (endereço, autenticação e lista). | Portabilidade (instalabilidade) |

**Base dos RNFs da área B.**

| RNF | Base |
|---|---|
| RNF-B1 | [Fato] suporte 24/7 citado pela SITA na sua solução de tomada de decisão colaborativa [53]; [Inferência] o valor de 99,5% é meta interna do projeto, porque o insumo deixa o valor "a definir". |
| RNF-B2 | [Inferência] conexão instável no pátio (insumo sem fonte); a precisão de minuto completo segue a convenção "5:59 is acceptable while 6:00 is not" [3] e a régua do horário-alvo de prontidão (TOBT) + 5 minutos [2] (ADR-0001), que depende do horário real da ação; o envio em até 5 segundos mantém a meta do objetivo 2 depois da reconexão. 30 minutos e 50 registros são valores de teste do projeto. |
| RNF-B3 | [Fato] aplicativos móveis para quem executa as tarefas [43][46] e checagens feitas no pátio [13]; [Inferência] versões e larguras de tela são escolha do projeto para cobrir celulares comuns. |
| RNF-B4 | [Inferência] produto web (`CONTEXT.md`, seção 1) usado por operadores de empresas diferentes, inclusive prestadores contratados, que não teriam um aplicativo instalado em comum. |

Fontes citadas: [2], [3], [13], [43], [46] e [53], conforme a numeração de `pesquisa/fontes.md`.
