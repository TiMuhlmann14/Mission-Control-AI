# Mission Control AI — Artemis Deep

Sistema inteligente de monitoramento de missão espacial experimental, desenvolvido para a **Global Solution 2026** da FIAP.

---

## Descrição do projeto

O **Mission Control AI** simula o monitoramento contínuo de uma missão espacial por meio de ciclos de análise. O sistema avalia cinco sensores críticos da nave — temperatura, comunicação, bateria, oxigênio e estabilidade — a cada ciclo, gera alertas automáticos, calcula o nível de risco e emite um relatório final com a situação da operação.

---

## Sobre a missão simulada

**Nome da missão: Artemis Deep**

**Nome da equipe: Equipe Asaph**

**Ciclos simulados: 8** 



**Narrativa dos ciclos:**
- Ciclo 1 — Início da missão (sistemas estáveis)
- Ciclo 2 — Primeiras anomalias (temperatura sobe, bateria cai)
- Ciclo 3 — Queda de comunicação (sinal deteriora)
- Ciclo 4 — Alerta de energia (bateria crítica)
- Ciclo 5 — Risco operacional total (múltiplos sistemas críticos)
- Ciclo 6 — Tentativa de recuperação
- Ciclo 7 — Estabilização progressiva
- Ciclo 8 — Recuperação confirmada

---

## Estrutura dos dados

A matriz principal `dados_missao` é uma lista de listas. Cada linha representa um ciclo da missão, com 5 valores nesta ordem:

```python
[temperatura, comunicacao, bateria, oxigenio, estabilidade]
```

| Posição | Sensor | Unidade |
|---|---|---|
| 0 | Temperatura interna | °C |
| 1 | Comunicação com a base | % |
| 2 | Sistema de energia (bateria) | % |
| 3 | Suporte de oxigênio | % |
| 4 | Estabilidade operacional | % |

---

## Regras de alerta

### Temperatura (°C)
| Condição | Classificação |
|---|---|
| Menor que 18 °C | ATENÇÃO |
| De 18 °C a 30 °C | NORMAL |
| De 30 °C a 35 °C | ATENÇÃO |
| Maior que 35 °C | CRÍTICO |

### Comunicação (%)
| Condição | Classificação |
|---|---|
| Menor que 30% | CRÍTICO |
| De 30% a 59% | ATENÇÃO |
| 60% ou mais | NORMAL |

### Bateria (%)
| Condição | Classificação |
|---|---|
| Menor que 20% | CRÍTICO |
| De 20% a 49% | ATENÇÃO |
| 50% ou mais | NORMAL |

### Oxigênio (%)
| Condição | Classificação |
|---|---|
| Menor que 80% | CRÍTICO |
| De 80% a 89% | ATENÇÃO |
| 90% ou mais | NORMAL |

### Estabilidade (%)
| Condição | Classificação |
|---|---|
| Menor que 40% | CRÍTICO |
| De 40% a 69% | ATENÇÃO |
| 70% ou mais | NORMAL |

---

## Pontuação e classificação de risco

Cada classificação gera uma pontuação:

| Classificação | Pontos |
|---|---|
| NORMAL | 0 |
| ATENÇÃO | 1 |
| CRÍTICO | 2 |

Com 5 sensores por ciclo, a pontuação máxima por ciclo é **10 pontos**.

| Pontuação total | Classificação do ciclo |
|---|---|
| 0 a 2 | MISSÃO ESTÁVEL |
| 3 a 5 | MISSÃO EM ATENÇÃO |
| 6 a 10 | MISSÃO CRÍTICA |

---

## Funções implementadas

| Função | Descrição |
|---|---|
| `analisar_temperatura()` | Classifica a temperatura e retorna pontuação |
| `analisar_comunicacao()` | Classifica a comunicação e retorna pontuação |
| `analisar_bateria()` | Classifica a bateria e retorna pontuação |
| `analisar_oxigenio()` | Classifica o oxigênio e retorna pontuação |
| `analisar_estabilidade()` | Classifica a estabilidade e retorna pontuação |
| `calcular_risco_ciclo()` | Soma as pontuações de um ciclo |
| `classificar_ciclo()` | Retorna a classificação com base na pontuação |
| `gerar_recomendacao()` | Gera recomendação automática baseada nos alertas |
| `analisar_tendencia()` | Compara primeiro e último ciclo |
| `identificar_area_mais_afetada()` | Soma pontuações por área e identifica a maior |
| `exibir_ciclo()` | Exibe a análise de um ciclo no terminal |
| `gerar_relatorio_final()` | Exibe o relatório consolidado da missão |

---

## Informações acadêmicas

- **Instituição:** FIAP
- **Turma: ** 1CCR
- **Disciplina:** Pensamento Computacional e Automação com Python
