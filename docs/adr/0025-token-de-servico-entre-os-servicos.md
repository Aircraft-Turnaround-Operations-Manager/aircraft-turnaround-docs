---
id: adr-0025
titulo: "ADR-0025 — Token de serviço nos pedidos entre os serviços"
tipo: decisao
decisao: D25
status: aceita
data: 2026-11-24
decisor: Rodrigo Alves
itens_template: [13, 14]
areas: [A, B, C, D]
fontes: []
relacionados: [adr-0016, adr-0023, adr-0015, adr-0020]
---
# ADR-0025 — Token de serviço nos pedidos entre os serviços

- **Status:** aceita, pela aprovação do Rodrigo Alves no pull request [#255](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/255). · **Data:** 24/11/2026 · **Decisor:** Rodrigo Alves · **Complementa:** [ADR-0016](0016-contrato-entre-os-servicos.md), pontos 2 e 3, e [ADR-0023](0023-interfaces-da-porta-de-entrada-e-do-cadastro.md), ponto 1

## Contexto

- Siglas usadas abaixo: requisito não funcional (RNF), token JSON assinado (JWT), transferência de estado representacional (REST), protocolo seguro de transferência de hipertexto (HTTPS) e segurança da camada de transporte (TLS).
- A ADR-0016 diz que os pedidos entre os serviços são REST sobre HTTPS (ponto 3), mas não diz como o serviço chamado confere quem chama.
- A ADR-0023, ponto 1, resolve as chamadas que vêm do site. A porta de entrada gera um token interno assinado com o usuário, válido por 60 s, e cada serviço "recusa a chamada sem token válido".
- Há também pedidos que um serviço faz direto a outro, sem passar pela porta de entrada. No item 13, são os métodos dos três clientes:
  - do Cadastro e Planejamento para a Execução em Solo (`ExecucaoEmSoloCliente`): por exemplo, `receberPlano`, `chegadaRegistrada` e `listarTarefasPendentes*`;
  - do Exceções e Liberação para a Execução em Solo (`ExecucaoEmSoloCliente`): por exemplo, `aplicarExcecao`, `reatribuir`, `liberar` e `consultarPedido`;
  - da Execução em Solo para o Cadastro e Planejamento (`CadastroCliente`): `listarOperadoresAtivos` (ADR-0023, ponto 3).

  Esses pedidos não levam o token interno. Pela regra da ADR-0023, ponto 1, seriam recusados. O RNF-1 pede a verificação a cada ação protegida, "inclusive acesso direto".
- Repassar o token do usuário não resolve. Ele vale 60 s, e alguns pedidos são reenviados sem usuário, depois de uma queda: a retomada do plano (ADR-0023, ponto 5) e o pedido pendente (ADR-0020). Por isso esses pedidos já levam o autor da ação como parâmetro (`autorId`).
- A dúvida foi registrada na [issue #207](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/207), achada no item 13.

## Opções consideradas

- **(a) Token de serviço assinado:** o mesmo mecanismo da ADR-0023, ponto 1, com o serviço no lugar do usuário.
- **(b) TLS mútuo (mTLS):** cada serviço tem um certificado, e a conexão HTTPS confere quem chama. Exige uma autoridade que emita e troque os certificados, inclusive na máquina de cada integrante (ADR-0016, ponto 4). Os serviços passariam a ter duas formas de conferir quem chama.
- **(c) Só a rede interna:** confiar em quem chega pela rede, sem conferir. Já foi descartada na ADR-0023, ponto 1: bastaria um serviço exposto na rede para alguém se passar por outro.

Foi escolhida a **(a)**.

## Decisão

1. **Token de serviço.** Cada serviço tem um par de chaves. Em cada pedido a outro serviço, ele gera um token JSON assinado (JWT) curto, com validade de 60 s, assinado com a sua chave privada. O token leva o nome do serviço que chama, o mesmo do campo `origem` do envelope dos avisos (ADR-0016, ponto 5), e não leva usuário.
2. **Conferência.** O serviço chamado confere a assinatura com a chave pública de quem chama e confere a validade. Depois, consulta uma lista fixa das rotas que cada serviço pode chamar. Recusa o pedido sem token válido ou de um serviço que não pode chamar aquela rota.
3. **Autor da ação.** O token de serviço não leva usuário. Quando o pedido nasce de uma ação de usuário, o autor continua no parâmetro `autorId`, gravado na trilha de auditoria (RNF-2).
4. **Reenvio.** Cada tentativa, inclusive a retomada depois de uma queda, gera um token novo. Por isso o reenvio não depende do token do usuário original.
5. **Fora do alcance do site.** A porta de entrada não encaminha chamadas do site às rotas entre serviços. Uma chamada do site que chegue a essas rotas por outro caminho vem sem token de serviço e é recusada (RNF-1, "inclusive acesso direto").
6. **Token válido.** Onde a ADR-0023, ponto 1, diz "token válido", vale o token interno do usuário, nas rotas do site, ou o token de serviço, nas rotas entre serviços. As duas rotas não se misturam.

## Consequências

- **Quem faz pedidos** (Cadastro e Planejamento, Exceções e Liberação e Execução em Solo) assina o token de serviço. **Quem atende** (Execução em Solo e Cadastro e Planejamento) confere o token e a lista de rotas. O Monitoramento não faz nem atende pedidos entre serviços: recebe tudo por aviso.
- **Item 13:** a seção do contrato diz que os clientes (`ExecucaoEmSoloCliente` e `CadastroCliente`) mandam o token de serviço. As assinaturas das rotas não mudam: o token, como o token interno, não aparece no diagrama.
- **Item 14:** os pedidos entre serviços podem citar este ponto, como os pedidos do site citam a ADR-0023, ponto 1.
- Requisitos funcionais, casos de uso, item 12, RNFs e telas não mudam.
- A lista de rotas por serviço segue os pedidos do item 13. Uma rota nova entre serviços entra na lista no mesmo pull request que a cria.

---

## Ligações

- **Contrato entre os serviços:** [ADR-0016](0016-contrato-entre-os-servicos.md) (complementada por esta)
- **Interfaces da porta de entrada:** [ADR-0023](0023-interfaces-da-porta-de-entrada-e-do-cadastro.md) (ponto 1 complementado por esta)
- **Divisão em microsserviços:** [ADR-0015](0015-divisao-em-microsservicos.md)
- **Pedido pendente:** [ADR-0020](0020-tecnologia-excecoes-e-liberacao.md)
- **Requisitos:** [Item 8 — área A](../../especificacao/08-requisitos-nao-funcionais/area-a.md) (RNF-1)
- **Diagrama de classes:** [Item 13](../../especificacao/13-diagrama-de-classes.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
