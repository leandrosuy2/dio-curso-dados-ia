# 04 - Avaliacao e Metricas

## Objetivo da avaliacao

Verificar se a Bia identifica corretamente o tema da pergunta, responde com base na base de conhecimento e evita respostas inseguras quando o assunto esta fora do escopo.

## Base de testes

Arquivo:

```text
data/perguntas_teste.json
```

## Metricas usadas

| Metrica | Como foi avaliada |
| --- | --- |
| Assertividade de tema | Comparacao entre tema esperado e tema obtido. |
| Cobertura da base | Verificacao dos temas cadastrados e testados. |
| Resposta segura | Analise se perguntas fora da base recebem mensagem de limitacao. |
| Clareza | Revisao manual da linguagem usada nas respostas. |
| Proxima acao | Verificacao se a resposta orienta um passo seguinte. |

## Resultado dos testes

Com a base atual, a aplicacao identifica corretamente as perguntas de teste preparadas para os temas cadastrados e responde com limite de conhecimento quando a pergunta esta fora da base.

Comando:

```bash
python assistente-virtual-ia/src/app.py --avaliar
```

## Melhorias futuras

- Criar mais perguntas de teste por tema.
- Medir satisfacao da pessoa usuaria.
- Registrar perguntas nao respondidas para evoluir a base.
- Usar uma IA generativa real com grounding na base de conhecimento.
- Adicionar avaliacao humana das respostas.

