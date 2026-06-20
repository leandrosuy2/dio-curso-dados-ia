# Miniguia de Estudos com NotebookLM: IA Generativa, LLMs e Engenharia de Prompts

Projeto desenvolvido para o desafio **Treinando uma IA de Aprendizagem: Explore o Poder do NotebookLM**, da DIO.

## Contexto

Este projeto explora o uso do **NotebookLM** como ferramenta de aprendizagem ativa para estudar **IA Generativa, Modelos de Linguagem de Grande Escala (LLMs) e Engenharia de Prompts**.

A proposta foi criar um caderno tematico capaz de reunir fontes confiaveis, organizar conceitos importantes e apoiar revisoes por meio de perguntas estrategicas. O foco nao foi apenas obter respostas prontas da IA, mas usar a ferramenta para comparar fontes, identificar lacunas de entendimento e transformar conteudo tecnico em material de estudo reutilizavel.

## Objetivos de estudo

- Entender o que e IA Generativa e como ela se diferencia de abordagens tradicionais de IA.
- Compreender, em nivel introdutorio, o papel dos LLMs em aplicacoes modernas.
- Aprender boas praticas de engenharia de prompts para melhorar respostas de modelos generativos.
- Criar um miniguia de estudo com resumo, glossario e prompts reutilizaveis.
- Documentar o raciocinio usado durante a interacao com a IA, incluindo ajustes e dificuldades encontradas.

## Ferramenta utilizada

- **NotebookLM**: usado como caderno tematico para carregar fontes, fazer perguntas, gerar resumos, comparar conceitos e criar materiais de revisao.

## Curadoria de fontes

As fontes abaixo foram selecionadas por serem abertas, introdutorias e diretamente relacionadas ao tema do caderno.

| Fonte | Tipo | Uso no projeto |
| --- | --- | --- |
| [Introduction to generative AI and agents - Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/fundamentals-generative-ai/) | Modulo online | Base para conceitos de IA generativa, LLMs, prompts e agentes. |
| [IA generativa - Google Cloud Documentation](https://docs.cloud.google.com/docs/generative-ai?hl=pt) | Documentacao | Visao geral de aplicacoes e recursos de IA generativa. |
| [Introducao a IA generativa - Google Skills](https://www.skills.google/course_templates/536?locale=pt_BR) | Curso introdutorio | Apoio para diferenciar IA generativa de machine learning tradicional. |
| [What is Generative AI? - IBM Think](https://www.ibm.com/think/topics/generative-ai) | Artigo tecnico | Definicao de IA generativa e exemplos de conteudo gerado. |
| [Prompt engineering techniques - Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering) | Documentacao tecnica | Boas praticas e estrutura para criar prompts mais eficazes. |

## Processo no NotebookLM

1. Criei um novo caderno tematico chamado **IA Generativa, LLMs e Prompts**.
2. Adicionei as fontes abertas listadas na curadoria.
3. Pedi ao NotebookLM uma visao geral do tema.
4. Testei prompts de resumo, comparacao, glossario e revisao.
5. Ajustei os prompts quando as respostas ficaram genericas ou pouco conectadas as fontes.
6. Consolidei os melhores resultados neste README.

## Engenharia de prompts e cicatrizes

Durante o uso da IA, alguns prompts iniciais geraram respostas amplas demais. Para melhorar os resultados, os prompts foram refinados com contexto, formato esperado e criterio de profundidade.

### Prompt 1: resumo geral

**Prompt testado:**

```text
Explique o que e IA generativa.
```

**Resultado observado:**

A resposta tende a ser correta, mas generica. Ela explica que IA generativa cria texto, imagem, codigo e outros conteudos, mas nao aprofunda muito a diferenca entre IA generativa, machine learning tradicional e LLMs.

**Ajuste realizado:**

```text
Com base apenas nas fontes adicionadas, explique o que e IA generativa em linguagem simples. Depois, compare IA generativa com machine learning tradicional e inclua 3 exemplos praticos de uso.
```

**Aprendizado:**

Prompts com contexto, restricao de fonte e formato esperado produzem respostas mais uteis para estudo.

### Prompt 2: comparacao entre conceitos

**Prompt testado:**

```text
Qual a diferenca entre IA generativa e LLM?
```

**Resultado observado:**

A resposta foi util, mas misturou os conceitos em alguns pontos. Foi necessario pedir uma comparacao estruturada.

**Ajuste realizado:**

```text
Crie uma tabela comparando IA generativa, LLMs e engenharia de prompts. Para cada item, apresente: definicao, funcao principal, exemplo de uso e risco comum.
```

**Aprendizado:**

Quando o assunto envolve conceitos proximos, tabelas ajudam a reduzir confusao.

### Prompt 3: revisao ativa

**Prompt testado:**

```text
Crie perguntas sobre o conteudo.
```

**Resultado observado:**

As perguntas ficaram simples demais e pareciam um questionario escolar basico.

**Ajuste realizado:**

```text
Crie 10 perguntas de revisao ativa sobre IA generativa, LLMs e prompts. Misture perguntas conceituais, perguntas de aplicacao pratica e perguntas que obriguem a comparar ideias. Inclua o gabarito comentado.
```

**Aprendizado:**

Pedir tipos diferentes de pergunta aumenta a qualidade da revisao.

### Prompt 4: glossario

**Prompt testado:**

```text
Faca um glossario.
```

**Resultado observado:**

O glossario ficou curto e sem exemplos.

**Ajuste realizado:**

```text
Monte um glossario com os principais termos do caderno. Para cada termo, traga uma definicao simples, um exemplo pratico e um erro comum de interpretacao.
```

**Aprendizado:**

Um bom prompt deve deixar claro o nivel de detalhe esperado.

## Miniguia de estudo

### 1. O que e IA Generativa?

IA Generativa e uma area da inteligencia artificial voltada para criar novos conteudos a partir de padroes aprendidos em dados. Esses conteudos podem incluir textos, imagens, codigos, resumos, respostas, roteiros, audios e outros formatos.

Diferente de sistemas tradicionais que apenas classificam, filtram ou preveem valores, modelos generativos conseguem produzir uma nova saida com base em uma instrucao. Por exemplo: responder uma pergunta, escrever um email, gerar um trecho de codigo ou resumir um documento.

### 2. O que sao LLMs?

LLMs, ou grandes modelos de linguagem, sao modelos treinados com grandes volumes de texto para compreender e gerar linguagem natural. Eles sao usados em chatbots, assistentes virtuais, ferramentas de resumo, geradores de codigo e sistemas de busca conversacional.

Um LLM nao "entende" como uma pessoa, mas identifica padroes estatisticos na linguagem e gera respostas provaveis com base no contexto recebido.

### 3. O que e Engenharia de Prompts?

Engenharia de prompts e a pratica de criar instrucoes claras para orientar melhor o comportamento de uma IA generativa. Um prompt bem elaborado informa o objetivo, o contexto, o formato da resposta, o publico-alvo e as restricoes.

Exemplo de prompt fraco:

```text
Explique LLM.
```

Exemplo de prompt melhor:

```text
Explique o que e um LLM para uma pessoa iniciante em tecnologia. Use uma analogia simples, cite 3 aplicacoes praticas e termine com uma pergunta de revisao.
```

### 4. Boas praticas de prompts

- Definir claramente a tarefa.
- Informar o publico-alvo da resposta.
- Pedir um formato especifico, como tabela, lista, resumo ou passo a passo.
- Fornecer contexto suficiente.
- Solicitar exemplos.
- Pedir que a IA use apenas as fontes carregadas quando o objetivo for estudo baseado em material confiavel.
- Refinar o prompt quando a resposta vier generica.

### 5. Limitacoes e cuidados

- A IA pode gerar respostas incorretas ou incompletas.
- As respostas devem ser conferidas com as fontes.
- Prompts vagos geram respostas vagas.
- Ferramentas de IA nao substituem pensamento critico.
- Em temas sensiveis, e importante validar informacoes em fontes oficiais.

## Glossario

| Termo | Definicao simples | Exemplo |
| --- | --- | --- |
| IA Generativa | Tipo de IA capaz de criar novos conteudos. | Gerar um resumo automatico de um artigo. |
| LLM | Modelo de linguagem treinado em grandes volumes de texto. | Chatbots que respondem perguntas em linguagem natural. |
| Prompt | Instrucao enviada para uma IA. | "Resuma este texto em 5 topicos." |
| Engenharia de Prompts | Tecnica de escrever prompts melhores para obter respostas melhores. | Pedir formato, contexto e exemplos na resposta. |
| Grounding | Uso de fontes especificas para ancorar a resposta da IA. | Responder apenas com base nos PDFs enviados ao NotebookLM. |
| Alucinacao | Resposta incorreta ou inventada pela IA. | Citar uma fonte inexistente. |
| Agente de IA | Sistema que usa IA para executar tarefas com algum nivel de autonomia. | Um assistente que pesquisa, resume e organiza informacoes. |
| Revisao ativa | Metodo de estudo baseado em perguntas e recuperacao da memoria. | Responder quizzes sem consultar o material. |

## Prompts reutilizaveis

### Resumo estruturado

```text
Com base apenas nas fontes deste caderno, crie um resumo estruturado sobre [TEMA]. Organize em: definicao, conceitos principais, exemplos praticos, riscos e pontos para revisar.
```

### Glossario inteligente

```text
Monte um glossario dos principais termos sobre [TEMA]. Para cada termo, inclua definicao simples, exemplo pratico e um erro comum de interpretacao.
```

### Plano de estudo

```text
Crie um plano de estudo de 7 dias sobre [TEMA], usando as fontes deste caderno. Para cada dia, inclua objetivo, conteudo a estudar, exercicio pratico e pergunta de revisao.
```

### Perguntas de revisao ativa

```text
Crie 10 perguntas de revisao ativa sobre [TEMA]. Misture perguntas faceis, intermediarias e aplicadas. Inclua gabarito comentado e indique quais fontes sustentam cada resposta.
```

### Comparacao de conceitos

```text
Compare [CONCEITO 1], [CONCEITO 2] e [CONCEITO 3] em uma tabela com: definicao, objetivo, exemplo de uso, limitacao e relacao com IA generativa.
```

### Explicacao para iniciante

```text
Explique [TEMA] para uma pessoa iniciante. Use linguagem simples, uma analogia, um exemplo do dia a dia e finalize com 3 perguntas para verificar entendimento.
```

## Resultado final

O caderno tematico no NotebookLM permitiu transformar fontes abertas sobre IA Generativa em um material de estudo mais organizado. A principal diferenca percebida foi que a IA se torna mais util quando recebe boas fontes e prompts bem definidos.

O projeto tambem mostrou que aprender com IA nao significa apenas pedir respostas, mas formular boas perguntas, comparar conceitos, revisar criticamente e registrar o caminho usado para chegar ao resultado.

## Como entregar na DIO

1. Criar um repositorio no GitHub com um nome como `miniguia-estudos-notebooklm`.
2. Enviar este README para o repositorio.
3. Copiar a URL principal do repositorio.
4. Na pagina do desafio da DIO, clicar em **Entregar Projeto**.
5. Colar o link do GitHub e adicionar uma breve descricao.

Sugestao de descricao para a entrega:

```text
Projeto criado para o desafio Treinando uma IA de Aprendizagem, usando o NotebookLM como caderno tematico para estudar IA Generativa, LLMs e Engenharia de Prompts. O repositorio documenta a curadoria de fontes, os prompts testados, dificuldades encontradas e um miniguia final de estudo.
```

