# Extraindo Insights do Feedback de Clientes Bancarios

Projeto desenvolvido para o desafio criativo **Extraindo Insights do Feedback de Clientes Bancarios**, da DIO.

## Contexto

Instituicoes financeiras recebem diariamente comentarios de clientes sobre aplicativos, atendimento, cartoes, tarifas, seguranca e servicos digitais como Pix. Esses feedbacks podem revelar dores recorrentes, pontos fortes da experiencia e oportunidades de melhoria.

Neste projeto, foi criada uma base simulada de feedbacks bancarios para aplicar uma analise exploratoria simples, classificando os comentarios por categoria, sentimento e prioridade. A partir dessa organizacao, foram extraidos insights acionaveis para melhorar a experiencia do cliente.

## Objetivos

- Organizar feedbacks de clientes bancarios em uma estrutura analisavel.
- Classificar cada comentario por tema principal.
- Identificar o sentimento predominante de cada feedback.
- Extrair padroes, problemas recorrentes e oportunidades de melhoria.
- Propor recomendacoes praticas para o banco.

## Base de dados

A base utilizada e simulada e esta disponivel no arquivo:

[feedbacks_clientes_bancarios.csv](feedbacks_clientes_bancarios.csv)

Ela contem as seguintes colunas:

| Coluna | Descricao |
| --- | --- |
| id | Identificador do feedback |
| feedback | Comentario do cliente |
| categoria | Tema principal do comentario |
| sentimento | Classificacao entre positivo, negativo ou neutro |
| prioridade | Nivel de atencao recomendado |

## Metodologia

1. Criei uma amostra de feedbacks simulando situacoes comuns em bancos digitais.
2. Classifiquei os comentarios em categorias como aplicativo, atendimento, Pix, cartao, tarifas e seguranca.
3. Analisei o sentimento de cada feedback.
4. Agrupei os principais problemas por recorrencia e impacto.
5. Transformei os padroes encontrados em insights e recomendacoes.

## Exemplos de feedbacks analisados

| Feedback | Categoria | Sentimento | Prioridade |
| --- | --- | --- | --- |
| O aplicativo trava toda vez que tento fazer Pix. | Pix/App | Negativo | Alta |
| O atendimento no chat demorou muito para responder. | Atendimento | Negativo | Alta |
| Gostei da facilidade para consultar saldo e extrato. | Aplicativo | Positivo | Baixa |
| As taxas do cartao de credito sao muito altas. | Tarifas/Cartao | Negativo | Media |
| Recebi alerta de seguranca rapidamente apos uma tentativa suspeita. | Seguranca | Positivo | Baixa |

## Analise dos feedbacks

### Distribuicao por sentimento

| Sentimento | Quantidade | Interpretacao |
| --- | ---: | --- |
| Negativo | 12 | A maior parte dos comentarios aponta dores na experiencia. |
| Positivo | 6 | Existem pontos fortes ligados a praticidade, seguranca e usabilidade. |
| Neutro | 2 | Comentarios informativos ou sugestoes sem carga emocional forte. |

### Principais categorias identificadas

| Categoria | Ocorrencias | Leitura do resultado |
| --- | ---: | --- |
| Aplicativo | 5 | Problemas de estabilidade e navegacao aparecem com frequencia. |
| Atendimento | 4 | Tempo de resposta e resolucao sao pontos sensiveis. |
| Pix e transferencias | 4 | Instabilidade em transacoes gera impacto alto na confianca. |
| Cartao e tarifas | 4 | Clientes reclamam de taxas, limite e clareza das cobrancas. |
| Seguranca | 3 | Feedbacks positivos sobre alertas, mas ha preocupacao com bloqueios. |

## Principais insights

### 1. Instabilidade no aplicativo afeta diretamente a confianca

Feedbacks sobre travamentos, lentidao e erro no Pix indicam que problemas tecnicos no app sao percebidos como falhas criticas. Em servicos bancarios, a confianca depende de disponibilidade e previsibilidade.

**Recomendacao:** priorizar monitoramento de estabilidade, testes em horarios de pico e comunicacao proativa quando houver indisponibilidade.

### 2. Atendimento lento aumenta a frustracao

Comentarios negativos sobre chat e suporte mostram que o cliente espera resolucao rapida, principalmente quando o problema envolve dinheiro parado, cartao bloqueado ou transacao pendente.

**Recomendacao:** criar triagem automatizada por urgencia e melhorar o encaminhamento para atendimento humano em casos sensiveis.

### 3. Pix e transferencias sao servicos de alta prioridade

Falhas no Pix aparecem como problema critico porque envolvem transacoes imediatas. Mesmo poucos erros podem gerar alto impacto emocional no cliente.

**Recomendacao:** acompanhar taxa de erro em Pix em tempo real e oferecer mensagens claras sobre status da transacao.

### 4. Clareza sobre tarifas ainda e uma dor importante

Alguns clientes demonstram insatisfacao com taxas do cartao e falta de previsibilidade sobre cobrancas.

**Recomendacao:** melhorar a explicacao das tarifas dentro do app, com simuladores, avisos antes da cobranca e linguagem mais simples.

### 5. Seguranca e valorizada quando e transparente

Alertas de seguranca foram bem avaliados, mas bloqueios sem explicacao geram inseguranca. O cliente quer protecao, mas tambem quer entender o motivo das acoes do banco.

**Recomendacao:** manter alertas rapidos, mas incluir explicacoes claras e caminhos simples para contestar bloqueios.

## Recomendações finais

- Melhorar estabilidade do aplicativo, principalmente em Pix e login.
- Reduzir tempo de resposta do atendimento no chat.
- Criar comunicacoes mais claras para erros de transacao.
- Explicar tarifas e limites com linguagem simples.
- Usar alertas de seguranca com orientacoes objetivas para o cliente.
- Criar painel interno de acompanhamento por sentimento e categoria.

## Prompts usados para apoiar a analise

```text
Classifique os feedbacks bancarios abaixo por categoria, sentimento e prioridade. Use categorias simples e explique o motivo da classificacao.
```

```text
Analise os feedbacks classificados e identifique os 5 principais problemas recorrentes. Para cada problema, sugira uma acao pratica de melhoria.
```

```text
Transforme a analise de feedbacks em um relatorio executivo curto, com insights acionaveis para uma equipe de experiencia do cliente em um banco digital.
```

```text
Crie uma tabela com categoria, quantidade de ocorrencias, sentimento predominante e recomendacao para o banco.
```

## Conclusao

A analise mostra que feedbacks de clientes podem ser transformados em informacoes estrategicas mesmo a partir de uma base simples. Ao classificar comentarios por tema, sentimento e prioridade, o banco consegue enxergar quais problemas afetam mais a experiencia e quais melhorias devem ser priorizadas.

Este desafio reforca como dados qualitativos, quando bem organizados, podem apoiar decisoes sobre produto, atendimento, seguranca e experiencia digital.

