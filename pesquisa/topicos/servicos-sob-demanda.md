---
id: servicos-sob-demanda
titulo: "Serviços sob demanda no turnaround (limpeza com risco biológico, assistência extra, catering adicional)"
tipo: pesquisa-topico
itens_template: [4, 6, 7, 10]
areas: [A, D]
decisoes: [D1, D2, D3, D6, D7]
fontes: [2, 16, 22, 34, 35, 40, 45, 46, 62, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]
relacionados: [atividades-e-dependencias, caminho-critico, tolerancias-e-indicadores, codigos-de-atraso, referencias-iata, a-cdm, marcos-e-horarios, inform-groundstar, assaia, sita, adb-safegate, veovo, matriz-comparativa, insumos-rfs]
status: vigente
atualizado: 2026-10-10
---
# Serviços sob demanda no turnaround

> Base de conhecimento do projeto · pesquisa dedicada de 10/10/2026 · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).

> **Decisões vigentes (prevalecem sobre o texto abaixo):** [D1 — Referência de horário: TOBT planejado + 5 min, unilateral](../../docs/adr/0001-referencia-horario-tobt-mais-5-min.md); [D2 — Metas percentuais do item 1: 80%](../../docs/adr/0002-metas-percentuais-80.md); [D3 — Antecipação de 5 min ou mais exige atualizar a previsão](../../docs/adr/0003-atualizar-previsao-na-antecipacao.md); [D6 — Códigos de atraso: tabela completa da ANAC (72 códigos)](../../docs/adr/0006-codigos-de-atraso-tabela-anac.md); [D7 — Dados registrados pelo operador, inclusive QR Code lido pelo celular](../../docs/adr/0007-dados-do-operador-e-qr-code.md).
>
> Esta pesquisa não muda nenhuma decisão. A régua continua sendo o horário-alvo de prontidão (TOBT) planejado + 5 min (D1), com meta de 80% (D2); a previsão vigente é atualizada quando a projeção se afasta 5 min ou mais (D3 e RF-D6); a causa de um atraso usa a tabela da Agência Nacional de Aviação Civil (ANAC) (D6); a confirmação de tarefa pode ser feita por leitura de código de resposta rápida (QR Code) no celular (D7).

## Pergunta

Como o mercado trata, no turnaround, serviços que **não acontecem em todo voo** mas precisam ser atendidos quando surgem: limpeza profunda de um assento porque um passageiro passou mal, limpeza com risco biológico, assistência extra a passageiro e catering adicional. Foram investigadas quatro frentes: (1) acordos e manuais de companhias aéreas e empresas de *handling*; (2) reguladores e autoridades; (3) tomada de decisão colaborativa em aeroportos (A-CDM); (4) softwares de turnaround.

## Resumo

1. **[Fato][67][68][69][70]** No Acordo Padrão de Atendimento em Solo (SGHA, *Standard Ground Handling Agreement*) da Associação Internacional de Transporte Aéreo (IATA), o Anexo A é o cardápio de serviços; o Anexo B de cada local diz quais foram contratados e tem uma seção própria de "ADDITIONAL SERVICES AND CHARGES". Contratos reais marcam itens como "(on request)" (limpeza interior, serviço de sanitário) e cobram à parte o que não está listado, com ordem de serviço assinada.
2. **[Fato][68][82][90]** Tempo padrão existe para alguns serviços: o modelo de acordo de nível de serviço (SLA) do Manual de Atendimento Aeroportuário (AHM) da IATA, na seção AHM 803, mede metas por voo; para assistência a passageiro com mobilidade reduzida (PRM) há metas de espera **diferentes para pedido avisado e não avisado**; para catering há tempos de logística citados por um fornecedor. **Não achei** tempo padrão público para limpeza profunda de assento ou limpeza com risco biológico.
3. **[Fato][73][74][78][80][81][86]** Quem aciona: a assistência a PRM é pedida na reserva, com 48 h de antecedência como boa prática (IATA) ou regra (União Europeia; ANAC, 48 ou 72 h), e nos EUA, em geral, não se pode exigir aviso prévio; a limpeza após evento a bordo é avisada pela tripulação às equipes de solo, durante o voo ou na chegada, sem antecedência fixa.
4. **[Fato][76]** No Brasil, a nova Resolução da Diretoria Colegiada (RDC) nº 1.038/2026 da Agência Nacional de Vigilância Sanitária (ANVISA) manda limpar e desinfetar compartimentos expostos a fluidos orgânicos "independente da duração da escala" e pede que a limpeza das escalas caiba no "tempo de solo previamente estabelecido". Ela ainda não está em vigor (150 dias após a publicação).
5. **[Fato][2][91][92][93]** No A-CDM, nenhuma fonte lida cita esses serviços pelo nome: a regra é genérica — o responsável atualiza o TOBT assim que souber de variação de 5 min ou mais; depois da emissão do horário-alvo de autorização de acionamento (TSAT), Hong Kong exige informar o motivo.
6. **[Fato][94][96][97][98][99]** Softwares de *handling* geram as tarefas do voo a partir de padrões contratados e permitem incluir tarefas ou serviços *ad hoc* durante a operação, em geral registrados para cobrança; o INFORM GroundStar recalcula o impacto nos processos dependentes e no TOBT. **Não achei** fornecedor que documente "tarefa opcional no modelo, ativada quando pedida".

---

## 1. Companhias aéreas e empresas de *handling*

### 1.1 Onde esses serviços ficam no acordo de *handling*

- **[Fato][67]** A IATA descreve o SGHA como acordo principal, "Annex A (list of services)" e "Annex B (location, agreed-on services, negotiated details, and charges)". O SLA é tratado à parte e "should be discussed, negotiated, and agreed upon along with the SGHA"; ele fica no "AHM803". A página é de 11/11/2022 e cita a 43ª edição do AHM, de 2023.
- **[Fato][68]** Em apresentação de 04/06/2025 a um grupo de trabalho do Ministério de Terras, Infraestrutura, Transporte e Turismo do Japão (MLIT), a IATA mostra: o acordo principal tem o artigo "5. STANDARD OF WORK"; o Anexo A tem oito seções, e a limpeza fica em "3. RAMP SERVICES"; o Anexo B tem, logo após os serviços contratados, a seção "2. ADDITIONAL SERVICES AND CHARGES".
- **[Fato][69]** Anexo B do SGHA (edição de jan/2013) da Czech Airlines Handling em Praga, vigência 2017–2020, publicado no Registro de Contratos da República Tcheca: serviços "not specifically listed in this Annex B" são cobrados pelas tarifas locais, e "A work order duly signed by either the Station representative or the Pilot will be produced along with the invoice." O mesmo anexo marca itens como "(on request and recharge)" (menor desacompanhado) e "(on request at extra charge)" (passageiro muito importante, VIP), o serviço de sanitário como "on request at separate charge" e manda fazer a limpeza da cabine "according to specifications in SLA – Service level Agreement that forms an integral part hereto". *Leitura de texto extraído de PDF digitalizado; valores das tarifas ilegíveis.*
- **[Fato][70]** Anexo B do SGHA (edição de jan/2018) entre Letiště Ostrava, a.s. e UG Jet, s.r.o., a partir de 01/05/2024: "3.10 Interior Cleaning (on request)"; "2.1.3 When requested by the Carrier," com, entre os itens, "persons with reduced mobility (PRMs)"; e "6.1 The Handling Company agrees to take all possible steps to ensure that, the agreed quality standards, will be met." Os padrões de qualidade não estão definidos no documento.
- **[Fato][71]** O aeroporto de Engadin (Suíça) publica condições próprias baseadas no Anexo A do SGHA: "As far as possible, Engadin Airport AG will, upon request, provide to the Client any additional services", e lista "Interior Cleaning (on request)".
- **[Fato][75]** A Swissport anuncia "night stop and deep cleans" e "rapid turnaround cleans", feitos "within defined turnaround windows", e diz que "Performance is tracked against agreed KPIs and reviewed regularly with airline partners" (KPI = indicador-chave de desempenho). A página não diz como os serviços são pedidos.
- **[Inferência]** O padrão que aparece nos contratos tem três camadas: (a) o Anexo A lista tudo o que pode ser prestado; (b) o Anexo B de cada local diz o que foi contratado, e parte vem marcada "on request" (presta-se só quando a companhia pede); (c) o que não está no Anexo B é serviço adicional, cobrado à parte e documentado por ordem de serviço. **Não achei**, nos contratos lidos, um item específico de "limpeza com risco biológico" ou "limpeza profunda de assento".

### 1.2 Tempo padrão e SLA

| Serviço | O que a fonte diz | Fonte |
|---|---|---|
| Qualquer serviço do Anexo A | O modelo de SLA (AHM 803) tem colunas de meta, ponto de medição, método, quem mede e período; o exemplo é de bagagem: "First bag shall be delivered to Baggage Claim by ATA + 20mins last bag to be delivered to Baggage Claim by ATA+ 40mins", medido "per flight" pela companhia (ATA = horário real de chegada). A IATA diz que o SLA formaliza os padrões combinados com base no artigo 5 do SGHA. | [Fato][68] |
| Assistência a PRM na chegada | Carta de qualidade do Aeroporto de Hamburgo (2008), com base no Regulamento (CE) nº 1107/2006 (art. 9.1) e no Doc 30 da Conferência Europeia de Aviação Civil (ECAC): pedido avisado — "80% of PRMs within 5 minutes of “on chocks”", 90% em 10 min, 100% em 20 min; pedido **não avisado** — "80% of PRMs within 25 minutes of “on chocks”", 90% em 35 min, 100% em 45 min. | [Fato][82] |
| Assistência a PRM na partida | Mesma carta, a partir da chegada do passageiro ao aeroporto: avisado — 80% em até 10 min, 90% em 20, 100% em 30; não avisado — 80% em até 25 min, 90% em 35, 100% em 45. | [Fato][82] |
| Catering | Anthony Colliss (Gate Gourmet Canada): "loading in the kitchen can take 15 to 30 minutes" e "leaving the kitchen, going through security and arriving at the aircraft can take 15 to 20 minutes"; em turnaround rápido, a equipe tenta chegar à aeronave junto com ela. | [Fato][90] |
| Limpeza profunda / com risco biológico | A orientação de limpeza da IATA (ed. 2, 2021) diz que a limpeza profunda (*deep cleaning*) está "NOT addressed in the scope of this document". | [Fato][73] |

- **Não achei** tempo padrão público para limpeza profunda de assento ou limpeza com risco biológico (nem nos resumos públicos do AHM e do Manual de Operações em Solo da IATA (IGOM), nem nos contratos e páginas de *handlers* lidos).
- **[Inferência]** Para catering adicional, os dois tempos citados em [90] somam de 30 a 50 min entre o início do carregamento na cozinha e a chegada à aeronave, sem contar o preparo; isso é uma soma feita aqui, não um número da fonte.
- **[Inferência]** A diferença entre pedido avisado e não avisado de PRM (5 min contra 25 min para 80% dos casos em [82]) mostra que o mesmo serviço tem tempo de resposta maior quando surge sem aviso.

### 1.3 Quem aciona e com que antecedência

- **Assistência a PRM.** **[Fato][74]** A IATA recomenda, como boa prática, que "assistance requests should be made no later than 48 hours before departure"; os códigos de solicitação de serviço especial (SSR) seguem o passageiro em todos os voos do itinerário; "Any request received after that deadline will be processed as per the booking channel opening times"; num dos casos descritos, "On the flight day, an automatic alert prompts airport staff to assist." As regras de cada país prevalecem.
- **Limpeza depois de evento a bordo.** **[Fato][73]** "flight crew should communicate with the appropriate ground operations handling teams regarding event details"; deve haver processo para a equipe de limpeza ser informada; se a tripulação de cabine começou a limpar em voo, avisa o destino para preparar a limpeza complementar. Depois de derramamento de fluidos corporais, "the aircraft cabin should be disinfected by ground cleaning crew or specially qualified personnel after disembarkation." **[Fato][86]** Os Centros de Controle e Prevenção de Doenças dos EUA (CDC) mandam a tripulação avisar a equipe de limpeza das áreas "needing more than routine cleaning or possible removal" e lembrar que "this situation may require additional PPE" (PPE = equipamento de proteção individual, EPI).
- **Serviço fora do contrato.** **[Fato][69]** A ordem de serviço é assinada pelo representante da companhia na estação ou pelo comandante.
- **Catering.** **[Fato][16]** Os códigos de atraso da IATA separam o código 17 (PC), "CATERING ORDER, late or incorrect order given to supplier", do código 37 (GB), "CATERING, late delivery or loading". **[Inferência]** O pedido de catering parte da companhia para o fornecedor; a entrega e o carregamento são do fornecedor.
- **Não achei** antecedência padrão para limpeza com risco biológico: nas fontes lidas ela é disparada pelo evento, avisada durante o voo ou constatada na chegada.

### 1.4 O que os manuais da IATA cobrem (sumários públicos)

- **[Fato][72]** O sumário do IGOM publicado pela IATA tem, no capítulo 3, a seção "3.7 A/C Cleaning & Disinfection", com "3.7.2 A/C Cleaning Intervals", "3.7.4 Cleaning & Disinfection Tasks", "3.7.5 A/C Cleaning & Disinfection During a Pandemic" e "3.7.6 Cleaning & Disinfection During an Event"; o capítulo 4 (Aircraft Turnaround) começa com "4.1.1 Actions Prior To Arrival". O documento não traz data nem edição.
- **[Fato][34][35]** IGOM e AHM são publicações pagas (ver [Referências da IATA](referencias-iata.md)). **Não confirmado:** o conteúdo da seção 3.7.6 e se ela define tempo ou forma de acionamento.

---

## 2. Reguladores e autoridades

### 2.1 Brasil — ANVISA

- **[Fato][76]** A RDC nº 1.038, de 21/08/2026, revoga a RDC nº 2/2003 (art. 120) e entra em vigor 150 dias após a publicação (art. 121). A cópia lida diz: "Republicada por ter saído no DOU de 24/08/2026, com incorreção" (DOU = Diário Oficial da União); **[Fato][77]** a AEROIN informa publicação em 25/08/2026. *A data exata e o texto certificado não foram conferidos no DOU.* Pelos dois casos, a vigência cai em janeiro de 2027.
- **[Fato][76]** Art. 78: as empresas aéreas mantêm um Plano de Gerenciamento de Limpeza e Desinfecção (PLD) com cronograma e procedimentos de rotina e "aqueles adotados pós-evento de saúde pública ou derrame de fluido biológico"; o § 1º manda considerar, entre outros, o tempo de solo; o § 2º diz: "Durante as escalas deve-se minimamente retirar resíduos sólidos e limpar e desinfetar os sanitários".
- **[Fato][76]** Art. 80: "Em caso de evento de saúde pública a bordo, ou situações de maior risco como compartimentos da aeronave expostos à contaminação por sangue, fezes, vômito, urina ou outros fluidos orgânicos", "deve-se realizar, independente da duração da escala, limpeza e desinfecção", com uso de EPI.
- **[Fato][76]** Art. 81: "O tempo destinado à execução dos procedimentos de limpeza e desinfecção de aeronaves em escalas ou pernoites deve ser compatível com a complexidade das ações previstas, bem como com o tamanho da aeronave." § 1º: "As empresas aéreas deverão se programar para que as atividades mencionadas no caput, as quais ocorram em escalas, sejam satisfatoriamente executadas, dentro do tempo de solo previamente estabelecido para as aeronaves." § 2º: "Casos fortuitos relacionados a ações de autoridades intervenientes na aviação civil que impactem a execução das atividades mencionadas no caput deverão ser devidamente registrados, juntamente com as evidências de tais ações."
- **[Fato][76]** A responsabilidade é da empresa aérea, inclusive nas atividades executadas por terceiros (arts. 11, 12 e 31). A norma não fala em liberação da aeronave nem em atraso.
- **Não li** a RDC nº 2/2003, que vale até a nova norma entrar em vigor.
- **[Inferência]** Quando a RDC nº 1.038/2026 vigorar, a limpeza depois de contato com fluidos orgânicos não é opcional para a companhia, mesmo em escala curta. A norma espera que ela caiba no tempo de solo, mas não diz o que fazer se não couber.

### 2.2 Brasil — ANAC

- **[Fato][78]** Resolução ANAC nº 280/2013 (texto compilado; o art. 26 tem redação dada pela Resolução nº 608/2021), art. 9º, § 1º: o passageiro com necessidade de assistência especial (PNAE) informa a necessidade "com antecedência mínima de 72 (setenta e duas) horas do horário previsto de partida do voo" quando precisa de acompanhante ou de documentos médicos, e "com antecedência mínima de 48 (quarenta e oito) horas do horário previsto de partida do voo" nos demais casos. Art. 17: o embarque do PNAE é feito "prioritariamente em relação a todos os demais passageiros". Art. 18: "O desembarque do PNAE deve ser realizado logo após o desembarque dos demais passageiros", salvo justificativa (ex.: conexão).
- **[Fato][79]** A Consulta Pública nº 02/2025 da ANAC propõe "substituir integralmente a atual Resolução" nº 280; recebeu contribuições de 24/01/2025 a 26/05/2025 e estava em análise na data da leitura. A proposta mantém 72 h quando a necessidade não foi informada na compra.
- **Não achei** norma da ANAC sobre limpeza de cabine com risco biológico; o tema sanitário está na ANVISA.
- **[Fato][16]** Os códigos de atraso da IATA têm o código 35 (GC), "AIRCRAFT CLEANING", e o 19 (PW), "REDUCED MOBILITY, boarding deboarding of passengers with reduced mobility". **[Inferência]** A tabela da ANAC usa as mesmas siglas (ver [Códigos de atraso](codigos-de-atraso.md) e D6).
- **[Inferência]** O art. 18 tem efeito no plano: a limpeza da cabine só começa depois do fim do desembarque ([Atividades e dependências](atividades-e-dependencias.md), A5, [22]); com PNAE a bordo, esse fim acontece depois da saída do PNAE.

### 2.3 União Europeia

- **[Fato][80]** O Regulamento (CE) nº 1107/2006 (da União Europeia, não da Agência da União Europeia para a Segurança da Aviação, EASA) dá direito à assistência quando a necessidade foi avisada "at least 48 hours before the published time of departure of the flight" (art. 7.1); sem aviso, "the managing body shall make all reasonable efforts to provide the assistance specified in Annex I" (art. 7.3); a companhia repassa o aviso ao aeroporto "at least 36 hours before the published departure time for the flight" (art. 6.2); o operador do aeroporto é "responsible for ensuring the provision of the assistance specified in Annex I" (art. 8.1).
- **[Fato][83][84][85]** A EASA orientou, na pandemia, a limpeza da aeronave "After removal of any COVID-19 suspected case" conforme o Boletim de Informação de Segurança (SIB) 2022-03, de 05/04/2022. O SIB dizia "This is information only. Recommendations are not mandatory." e pedia desinfecção, para caso confirmado até 48 h depois do voo, "as soon as operationally possible and, preferably, no later than 24 hours after receiving the information". Em 29/06/2023, EASA e o Centro Europeu de Prevenção e Controle de Doenças (ECDC) retiraram o protocolo conjunto e o SIB 2022-03.
- **Não achei** regra vigente da EASA sobre limpeza de cabine com fluidos corporais nem sobre o tempo que ela pode tomar.

### 2.4 Estados Unidos

- **Não achei** norma da Administração Federal de Aviação dos EUA (FAA) sobre limpeza de cabine com risco biológico.
- **[Fato][81]** A regra de acessibilidade 14 CFR 382.27 (CFR = Código de Regulamentos Federais dos EUA) é do Departamento de Transportes dos EUA (DOT), não da FAA. Em geral, "you must not require a passenger with a disability to provide advance notice"; para uma lista de serviços (oxigênio, maca, grupo de dez ou mais etc.), a companhia pode exigir "48 hours' advance notice and check-in one hour before the check-in time for the general public"; o aviso deve ser repassado "clearly and on time, to the people responsible for providing the requested service" (§ e); sem aviso, a companhia ainda presta o serviço se puder fazê-lo "by making reasonable efforts, without delaying the flight" (§ g).
- **[Fato][86]** Orientação do CDC para tripulação (atualizada em 15/05/2024): material contaminado vai em saco de risco biológico; a equipe de limpeza é avisada das áreas que pedem mais que a limpeza de rotina.
- **[Fato][87]** No caso extremo de viajante com sintomas de febre hemorrágica viral, a aeronave "should be taken out of service immediately" e "can be held until the laboratory-confirmed diagnosis has been obtained" (CDC, 17/04/2024). **[Inferência]** Nesse caso já não é um serviço dentro do turnaround: a aeronave sai de operação.

### 2.5 Organização Mundial da Saúde (OMS)

- **[Fato][88]** O guia de higiene e saneamento na aviação da OMS (3ª ed., 2009) diz que "it is necessary for aircraft and airport operators and ground handling agents to have a coordinated plan in place" para aeronave afetada ou pessoa com doença transmissível, e que o treinamento deve dar ênfase aos procedimentos disparados por evento, menos familiares que a limpeza de rotina. *As seções 3.2.4 e a diretriz 3.6 (desinfecção depois de evento) não vieram na extração do texto.*

### 2.6 Impacto no horário: o que as fontes dizem

- **[Fato][76]** A ANVISA manda fazer a limpeza depois de fluido orgânico "independente da duração da escala" e pede programação para caber no tempo de solo (arts. 80 e 81).
- **[Fato][73]** A IATA pede que a companhia avalie "its impact on the operations", inclusive nos tempos de solo, ao definir seus procedimentos de limpeza.
- **[Fato][81]** Nos EUA, pedido de assistência sem aviso é atendido se possível "without delaying the flight".
- **[Fato][89]** Caso Air Canada (voo de 26/08/2023, Las Vegas–Montreal): passageiras foram retiradas depois de reclamar de assentos sujos de vômito; a companhia declarou que "Our operating procedures were not followed correctly in this instance", e a agência de saúde pública do Canadá entrou em contato com ela. Na mesma reportagem, um especialista diz que "You'd be extending the ground time on the airplane to do the clean-up", e um ex-diretor de operações da empresa diz que as almofadas dos assentos "are removable" e costumam ser trocadas por equipes contratadas "in relatively short order".
- **[Inferência]** Há tensão entre a obrigação de limpar e o horário, e nenhuma fonte lida dá uma duração padrão para isso. Na prática, a duração depende do que é feito (desinfetar a superfície ou trocar a almofada do assento).

---

## 3. A-CDM: horário-alvo de prontidão (TOBT) e atualização da previsão

- **[Fato][2]** Especificação da EUROCONTROL (2025): a companhia aérea "is also responsible for the TOBT and any updates" (§ 4.7) e pode delegar ao *handling* (§ 4.6); o *handling* atualiza o TOBT "Should availability of resources to carry out the turnaround affect the TOBT for a flight" (§ 4.6); "At each step of the flight progress, the TOBT may be updated" (§ 5.2.1); depois da chegada à posição, o TOBT calculado é o horário real de chegada à posição (AIBT) mais o tempo mínimo de turnaround (MTTT) (§ 5.1.7.3); o responsável é avisado se a prontidão não foi registrada até TOBT + 5 min (§ 5.1.11.3); sem atualização até TOBT + 10 min, o TOBT é removido (§ 5.2.2). Entre as causas de volta à posição, a especificação cita "misbehaving passenger" (§ 5.2.4).
- **[Fato][92]** Genebra: "The TOBT must be updated by the handling agent as soon as he is aware of variation in readiness of a flight", para variação de 5 min ou mais, para mais ou para menos.
- **[Fato][91]** Munique: atualizar o TOBT "Generally, as early as you learn of the handling delays yourself"; depois da emissão do TSAT, o TOBT pode ser atualizado no máximo três vezes.
- **[Fato][93]** Hong Kong (diretrizes v2.0, 20/10/2018): a previsão automática "may not always accurately predict" a prontidão, "especially for cases of delays caused by turnaround activities"; depois da emissão do TSAT, a mudança exige "input the reason for the change"; num exemplo, um passageiro ausente obrigou a retirar bagagem e a companhia ou o *handling* informou novo TOBT com o motivo.
- **Não achei**, nas fontes de A-CDM lidas, menção específica a limpeza com risco biológico, a PRM sem aviso ou a catering adicional como causa de atualização do TOBT. A regra é genérica: qualquer variação de 5 min ou mais.
- **[Inferência]** No projeto, isso já está coberto pelo RF-D6 (pedido de atualização do TOBT quando a projeção se afasta 5 min ou mais do TOBT vigente). O ponto aberto é **como o serviço sob demanda entra na projeção**: se ele não vira tarefa do plano, a projeção não o enxerga.

---

## 4. Softwares de turnaround

Todas as linhas são **declarações do fornecedor** nas páginas lidas.

| Produto | Como inclui tarefa ou serviço fora do padrão | Efeito no plano e nos alertas | Fonte |
|---|---|---|---|
| INFORM GroundStar (TurnManager, TeamWork, PRM) | TeamWork avisa a equipe de "delays or changes that may affect them"; o gestor ajusta manualmente ou aceita a recomendação. A solução de PRM dá "more flexibility to fulfill ad-hoc PRM requests". Não achei descrição de tarefa opcional no modelo. | TurnManager: "the system will automatically calculate its impact on the subsequent dependent handling processes"; "Constant re-calculation of deviations in the overall turnaround", que culmina no cálculo do TOBT; "all relevant stakeholders are instantly notified on their desktops or mobile devices". | [Fato][45][46][94][95] |
| TAV Technologies GHS | Gera tarefas "based on engagement standards from received flights" e faz "real-time operational, ad-hoc, and break task planning". | "can provide notifications about required actions and flight changes". | [Fato][96] |
| EPG Ground Handling System | "All services that go beyond the original contract are recorded as ad hoc services", cobrados pela tarifa publicada. | Não informado. | [Fato][97] |
| Tarmac Technologies AGOA | Registro para "ensure all additional services are properly invoiced". | "custom alert-rules to notify you as soon as a turnaround might be going off track". | [Fato][98] |
| Zafire FirstPRM | "efficient management of planned and 'on the fly' jobs" de assistência a PRM. | Trabalhos com risco de estourar o SLA ("hot jobs") ficam destacados por cor. | [Fato][99] |
| ADB SAFEGATE AiPRON 360 | O *handling* pode "adjust tasks in response to changing conditions"; inclusão de tarefa nova não descrita. | Alertas de "deviations from predicted off-block times, or impending delays". | [Fato][100] |
| SITA (Mobile Resource Manager) | Não descreve inclusão de tarefa *ad hoc*. | "Predict delayed milestones and their domino effects to make better decisions." | [Fato][101] |
| Veovo (Resource Management) | "helps you adjust to day-of-operations events"; nada específico. | Não informado. | [Fato][102] |
| Assaia (TurnaroundControl) | Os eventos vêm de câmeras; não documenta inclusão de tarefa *ad hoc*. | Alertas com "Airline-specific business logic". | [Fato][40] |

- **[Inferência]** Aparecem três mecanismos: (a) **tarefa gerada por regra** a partir dos dados do voo e do contrato (TAV [96]); (b) **tarefa ou serviço *ad hoc* incluído durante a operação**, quase sempre ligado à cobrança do serviço adicional (EPG [97], Tarmac [98], TAV [96]) ou à fila de atendimento de PRM (Zafire [99], INFORM [95]); (c) **recálculo do impacto e alerta** (INFORM TurnManager [45][94], AiPRON [100], SITA [101]).
- **Não achei** fornecedor que documente uma "tarefa opcional" pré-modelada, ativada quando pedida, nem detalhe de como a tarefa *ad hoc* entra nas dependências do plano.

---

## 5. Impacto possível (opções para o grupo, sem decisão)

> RF-A4 a RF-A8 conforme o texto do PR #79 (branch `ra1/t06-a-requisitos-funcionais`), ainda não integrado à `main` em 10/10/2026. RF-D7 conforme a `main`. As opções abaixo são [Inferência] apoiadas nas fontes indicadas; nenhuma muda texto da especificação.

### Área A — modelo de tarefas e plano (RF-A4 a RF-A8)

| # | Opção | Base | Prós | Contras e pontos de atenção |
|---|---|---|---|---|
| A-1 | **Catálogo de serviços sob demanda no modelo (RF-A4):** tarefas cadastradas como "sob demanda", que não entram no plano até serem acionadas; levam tipo, equipe, duração e pontos de QR Code (RF-A7). | Anexo B com itens "on request" [69][70]; tarefas por padrão contratado [96] | O serviço já tem equipe, duração e pontos prontos quando surge; espelha o contrato. | Atributo novo em RF-A4, além de obrigatoriedade e "Não aplicável"; RF-A6 precisaria dizer se a cópia leva o catálogo. |
| A-2 | **Tarefa opcional com o que já existe:** tarefa não obrigatória e com "Não aplicável" permitido, sempre copiada (RF-A6) e marcada "Não aplicável" quando não pedida. | RF-A4 e RF-B5 atuais | Nada novo no modelo. | O operador marca "Não aplicável" em quase todo turnaround, com justificativa (RF-B5); polui o plano; depende da área B. |
| A-3 | **Serviço conhecido antes de o plano começar** (PRM avisado em 48 h, catering extra já pedido): incluir no plano inicial (RF-A5) com dependências (RF-A8), por exemplo "desembarque do PNAE" antes da limpeza. | ANAC art. 18 [78]; aviso de 48 h [74][80] | Usa RF-A5 e RF-A8 como estão. | Só vale antes do início das tarefas (RF-A5, RF-A6 e RF-A8 congelam o plano); pede A-1 ou A-2 para a tarefa existir no modelo. |
| A-4 | **Duração do serviço como parâmetro local** (o "duração positiva" de RF-A4). | Falta de tempo padrão público para limpeza com risco biológico (seção 1.2); metas de PRM de [82] são de espera, não de duração | Cada operador ajusta ao seu contrato e SLA. | Sem número de referência do setor para citar. |

### Área D — replanejamento durante a operação (RF-D7)

| # | Opção | Base | Prós | Contras e pontos de atenção |
|---|---|---|---|---|
| D-1 | **Ampliar o RF-D7 para incluir tarefa no plano em andamento** (do catálogo A-1 ou livre), com responsável, janela e dependências, registrando autor, horário e motivo, e recalculando projeção e caminho crítico. | *Ad hoc* em tempo real [96][97]; recálculo do impacto [45][94] | O serviço vira tarefa: entra na projeção, no caminho crítico e no bloqueio de liberação; pode ter confirmação por QR Code (D7). | Hoje o RF-D7 só altera janela e dependências de tarefa não iniciada; a US-D7 e o caso de uso da área D teriam de acompanhar. |
| D-2 | **Manter o RF-D7 e tratar como exceção (RF-D1)** com o código da ANAC (ex.: GC limpeza, PW mobilidade reduzida, GB catering — siglas iguais às da IATA, conforme a inferência registrada na D6). | D6; códigos [16][62] | Nada novo na área D. | Sem tarefa própria: o tempo gasto só aparece como atraso das tarefas existentes; não há responsável nem confirmação do serviço. |
| D-3 | **Exceção + tarefa:** a exceção (RF-D1) registra a causa e a tarefa incluída (D-1) registra a execução. | D-1 + D-2 | Separa "por que atrasou" de "o que foi feito". | Dois registros para um evento. |
| D-4 | **Pedido de atualização do TOBT:** em qualquer opção, se o serviço entra na projeção, o RF-D6 pede atualização quando o afastamento chegar a 5 min; pode-se pedir também o motivo da mudança, como em Hong Kong. | A-CDM [2][91][92][93]; D3 | Alinha ao A-CDM sem regra nova de horário. | Pedir motivo na atualização seria acréscimo ao RF-D6. |
| D-5 | **Serviço obrigatório bloqueia a liberação:** se a limpeza com risco biológico for incluída como obrigatória, o RF-D4 já recusa a liberação enquanto ela estiver pendente. | ANVISA art. 80 [76], quando vigorar | Usa o bloqueio que já existe. | Depende de a tarefa existir no plano (D-1). |

### Dúvidas para o grupo (não decididas)

1. **Meta do objetivo 1:** um atraso causado por serviço sob demanda legítimo (ex.: limpeza obrigatória pela ANVISA) conta contra os 80% (D1 e D2)? Mudar isso mexe em decisão; fica registrado como dúvida, sem proposta.
2. **Quem aciona no sistema:** só o Coordenador de Turnaround, ou o Operador de Solo/Rampa também pode registrar que encontrou a necessidade (ex.: a equipe de limpeza acha vômito no assento)? A segunda opção toca a área B.
3. **Pendências cruzadas:** A-2 depende do RF-B5 (área B); alertas para serviço sob demanda em risco dependem da área C. Se uma dessas opções for escolhida, registrar na issue `pendencia-cruzada` da área correspondente (AGENTS.md, regra 8).

---

## Ligações

- **Decisões:** [D1](../../docs/adr/0001-referencia-horario-tobt-mais-5-min.md), [D2](../../docs/adr/0002-metas-percentuais-80.md), [D3](../../docs/adr/0003-atualizar-previsao-na-antecipacao.md), [D6](../../docs/adr/0006-codigos-de-atraso-tabela-anac.md), [D7](../../docs/adr/0007-dados-do-operador-e-qr-code.md)
- **Itens da especificação:** [Item 4 — Mapeamento de Negócios (BPMN TO BE)](../../especificacao/04-mapeamento-de-negocios.md), [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 7 — Estórias de Usuário](../../especificacao/07-estorias-de-usuario/00-item.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md)
- **Áreas do plano RA1:** [Área A — Acesso e planejamento](../../especificacao/06-requisitos-funcionais/area-a.md), [Área D — Exceções e liberação](../../especificacao/06-requisitos-funcionais/area-d.md) (divisão em [entregas/ra1-tarefas.md](../../entregas/ra1-tarefas.md), tabela 1.2)
- **Relacionados:** [atividades-e-dependencias](atividades-e-dependencias.md), [caminho-critico](caminho-critico.md), [tolerancias-e-indicadores](tolerancias-e-indicadores.md), [codigos-de-atraso](codigos-de-atraso.md), [referencias-iata](referencias-iata.md), [a-cdm](a-cdm.md), [marcos-e-horarios](marcos-e-horarios.md), [inform-groundstar](../similares/inform-groundstar.md), [assaia](../similares/assaia.md), [sita](../similares/sita.md), [adb-safegate](../similares/adb-safegate.md), [veovo](../similares/veovo.md), [matriz-comparativa](../similares/matriz-comparativa.md), [insumos-rfs](../impacto/insumos-rfs.md)
- **Fontes citadas:** 2, 16, 22, 34, 35, 40, 45, 46, 62, 67 a 102 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
