# aircraft-turnaround-docs

Repositório de documentação do projeto **Aircraft Turnaround Orchestration System**, da disciplina Especificação de Software (PSI151), BSI PUCPR, 6º período, 2026.

## Entrega RA1: especificação (itens 1 a 11)

- Plano de tarefas: [`entregas/ra1-tarefas.md`](entregas/ra1-tarefas.md)
- Critérios de aceite (Definition of Done): [`entregas/ra1-criterios-de-aceite.md`](entregas/ra1-criterios-de-aceite.md)
- Board: GitHub Project **"Especificação de Software - 6p"** (issues com o rótulo `ra1`)

## Convenções

### Nome do produto

Usar **Aircraft Turnaround Orchestration System**, exatamente assim, em todos os campos "NOME DO PRODUTO" / "PRODUTO" dos quadros (critério X.9).

### Estrutura de arquivos

Há um arquivo ou pasta por item do template, com o número e o título original. O documento final é a concatenação dos arquivos `.md` de `especificacao/` em **ordem alfabética de caminho**, que coincide com a ordem do template.

```
especificacao/
├── 01-3-objetivos.md                       # T01
├── 02-e-nao-e-faz-nao-faz.md               # T02
├── 03-visao-do-produto.md                  # T03
├── 04-mapeamento-de-negocios.md            # T04
├── 05-atores-usuarios.md                   # T05
├── 06-requisitos-funcionais/               # T06
│   ├── 00-item.md                          #   título + justificativa da priorização (tarefa-mãe)
│   └── area-a.md … area-d.md               #   RFs de cada área (sub-issues T06-A…D)
├── 07-estorias-de-usuario/                 # T07: 00-item.md + area-a.md … area-d.md
├── 08-requisitos-nao-funcionais/           # T08: 00-item.md + area-a.md … area-d.md
├── 09-diagrama-geral-de-casos-de-uso.md    # T09
├── 10-especificacoes-de-caso-de-uso/       # T10: 00-item.md + area-a.md … area-d.md
│   └── prototipos/                         #   imagens dos protótipos de tela (ucNN-<tela>.png)
├── 11-diagrama-de-atividades.md            # T11
└── diagramas/                              # fontes e imagens exportadas dos diagramas
```

- **Itens por integrante (6, 7, 8 e 10):** cada área (tabela 1.2 do plano) edita **apenas o seu `area-x.md`**, assim não há conflito de merge entre integrantes. O `00-item.md` é da tarefa-mãe.
- **Tabelas dos itens 6 e 8:** cada `area-x.md` tem a tabela com o mesmo cabeçalho do template. Na consolidação, as 4 tabelas viram uma só: fica o cabeçalho da área A e as linhas das áreas B a D são anexadas em seguida.
- **Numeração fixa por área:** A = RF-1 a RF-4, B = RF-5 a RF-8, C = RF-9 a RF-12, D = RF-13 a RF-16. O mesmo vale para USnnn, UCnn e RNF-n.
- Os comentários `<!-- ... -->` nos arquivos são orientações para quem escreve. Eles não aparecem no documento renderizado e devem ser apagados quando o item estiver pronto.

### Diagramas

- Escritos como código em **Mermaid** (`.mmd`) ou **PlantUML** (`.puml`), o que funcionar melhor para cada diagrama.
- A fonte e a imagem exportada (`.png`) ficam juntas em `especificacao/diagramas/`, com o mesmo nome base: `04-bpmn-to-be`, `09-casos-de-uso`, `11-atividades`.
- O MD do item referencia a imagem: `![Diagrama Geral de Casos de Uso](diagramas/09-casos-de-uso.png)`.

### Branches e pull requests

- Uma branch por tarefa, com o padrão `ra1/<tarefa>-<descricao-curta>` em minúsculas e sem acentos. Exemplos: `ra1/t01-3-objetivos`, `ra1/t06-a-rfs-area-a`, `ra1/t10-c-casos-de-uso-area-c`.
- Ao começar, quem puxar a tarefa se atribui como responsável (assignee) e move o card para **In progress**.
- O trabalho entra na `main` só por **pull request**. O título do PR é o título da issue e o corpo traz `Closes #<n>` e a evidência de cada critério. Com o PR aberto, o card vai para **In review**; outro integrante revisa, e o card só vai para **Done** depois do merge.

### Consolidação (T13)

Depois que todos os itens estiverem na `main`, os MDs são consolidados em um único documento na ordem e com os títulos do template (capa, sumário, seções 1 a 11 e declaração de uso de IA) e exportados em **PDF** para envio no Canvas.
