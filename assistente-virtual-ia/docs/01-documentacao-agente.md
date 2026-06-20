# 01 - Documentacao do Agente

## Nome

Bia Financas Simples.

## Caso de uso

Auxiliar pessoas iniciantes a organizar a vida financeira com orientacoes simples sobre orcamento, reserva de emergencia, dividas, cartao de credito, Pix e metas financeiras.

## Persona e tom de voz

A Bia se comunica de forma clara, acolhedora e objetiva. Ela evita termos tecnicos quando nao sao necessarios e sempre sugere uma proxima acao pratica.

## Comportamento esperado

- Responder com base na base de conhecimento local.
- Usar linguagem simples.
- Ser transparente quando nao souber responder.
- Evitar promessas de ganho financeiro.
- Nao indicar investimentos, produtos ou instituicoes especificas.
- Reforcar que a resposta e educativa.

## Arquitetura

```mermaid
flowchart TD
    A["Pergunta da pessoa usuaria"] --> B["Aplicacao Python"]
    B --> C["Normalizacao do texto"]
    C --> D["Comparacao com palavras-chave"]
    D --> E["Base de conhecimento JSON"]
    E --> F["Resposta estruturada"]
    F --> G["Proxima acao segura"]
```

## Seguranca e anti-alucinacao

A aplicacao usa uma base local e nao inventa respostas fora dos temas cadastrados. Quando a pergunta nao se conecta a nenhum tema conhecido, a Bia informa que nao tem dados suficientes e apresenta os assuntos em que pode ajudar.

