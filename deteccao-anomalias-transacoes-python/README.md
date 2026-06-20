# Deteccao de Anomalias em Transacoes em Python

Projeto desenvolvido para o desafio **Deteccao de Anomalias em Transacoes em Python**, da DIO.

## Contexto

Instituicoes financeiras monitoram transacoes diariamente para identificar comportamentos suspeitos, como valores muito acima do padrao, compras em horarios incomuns, acessos de paises diferentes ou sequencias de operacoes fora do perfil do cliente.

Neste projeto, foi criada uma base simulada de transacoes bancarias e um script em Python para detectar possiveis anomalias usando regras simples e interpretaveis.

## Objetivos

- Criar uma base de transacoes simuladas.
- Analisar valores, horarios, paises e tipos de transacao.
- Detectar transacoes suspeitas com base em criterios estatisticos e regras de negocio.
- Gerar uma saida consolidada com as anomalias encontradas.
- Documentar o raciocinio usado na deteccao.

## Estrutura do projeto

```text
deteccao-anomalias-transacoes-python/
├── README.md
├── transacoes.csv
├── detectar_anomalias.py
├── anomalias_detectadas.csv
└── ENTREGA_DIO.md
```

## Base de dados

O arquivo [transacoes.csv](transacoes.csv) contem transacoes simuladas com as seguintes colunas:

| Coluna | Descricao |
| --- | --- |
| id_transacao | Identificador da transacao |
| cliente_id | Identificador do cliente |
| valor | Valor da transacao em reais |
| tipo | Tipo da transacao |
| pais | Pais onde a transacao ocorreu |
| hora | Hora da transacao |
| canal | Canal utilizado |

## Criterios de anomalia

O script marca uma transacao como suspeita quando encontra um ou mais dos seguintes sinais:

| Criterio | Explicacao |
| --- | --- |
| Valor muito alto | Transacao com z-score acima de 2 em relacao aos valores da base. |
| Valor acima de R$ 5.000 | Regra direta para capturar operacoes de alto impacto. |
| Horario incomum | Transacao realizada entre 00h e 05h. |
| Pais diferente do Brasil | Possivel comportamento fora do padrao esperado. |
| Saque alto | Saques acima de R$ 2.000 recebem atencao especial. |

## Como executar

No terminal, acesse a pasta do projeto e execute:

```bash
python detectar_anomalias.py
```

O script le o arquivo `transacoes.csv` e gera o arquivo `anomalias_detectadas.csv`.

## Exemplo de saida

```text
Total de transacoes analisadas: 25
Total de anomalias encontradas: 8
Arquivo gerado: anomalias_detectadas.csv
```

## Principais insights

### 1. Transacoes internacionais aparecem como ponto de atencao

Operacoes realizadas fora do Brasil foram classificadas como suspeitas porque podem indicar uso indevido do cartao ou acesso incomum.

### 2. Valores muito altos concentram maior risco

Transacoes acima de R$ 5.000 ou muito distantes da media da base precisam de verificacao adicional, principalmente quando combinadas com horario incomum.

### 3. Horario da madrugada aumenta o nivel de suspeita

Transacoes entre 00h e 05h podem ser legitimas, mas merecem monitoramento quando combinadas com valor alto, pais diferente ou saque.

### 4. Regras simples ja ajudam na triagem

Mesmo sem modelos avancados de machine learning, regras estatisticas e de negocio conseguem destacar transacoes que devem ser analisadas por uma equipe antifraude.

## Limitacoes

- A base e simulada e pequena.
- O metodo usa regras simples, nao um modelo treinado.
- Em um ambiente real, seria importante analisar historico individual de cada cliente.
- O z-score considera a base inteira, mas o ideal seria comparar cada cliente com seu proprio padrao.

## Possiveis melhorias

- Usar bibliotecas como pandas e scikit-learn.
- Aplicar algoritmos como Isolation Forest ou Local Outlier Factor.
- Criar analise por perfil de cliente.
- Adicionar visualizacoes graficas.
- Integrar alertas em tempo real.

## Conclusao

O projeto demonstra como Python pode ser usado para identificar anomalias em transacoes financeiras de forma simples, clara e explicavel. A abordagem combina estatistica basica e regras de negocio para gerar uma lista de transacoes suspeitas que podem ser investigadas posteriormente.

