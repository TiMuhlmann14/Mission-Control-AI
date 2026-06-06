# ============================================================
# MISSION CONTROL AI
# GS2026.1 - Pensamento Computacional e Automação com Python
# ============================================================

# --- Dados da missão ---
NOME_MISSAO = "Artemis Deep Scan"
NOME_EQUIPE  = "Equipe Nebula"

# Matriz principal: [temperatura, comunicacao, bateria, oxigenio, estabilidade]
# Ciclo 1 — Início da missão         (sistemas estáveis)
# Ciclo 2 — Primeiras anomalias      (temperatura sobe, bateria cai)
# Ciclo 3 — Queda de comunicação     (sinal deteriora)
# Ciclo 4 — Alerta de energia        (bateria crítica)
# Ciclo 5 — Risco operacional total  (múltiplos sistemas críticos)
# Ciclo 6 — Tentativa de recuperação (sistemas parcialmente estabilizados)
# Ciclo 7 — Estabilização progressiva
# Ciclo 8 — Recuperação confirmada
dados_missao = [
    [22, 95, 91, 98, 93],   # Ciclo 1
    [26, 83, 76, 95, 87],   # Ciclo 2
    [32, 61, 54, 92, 72],   # Ciclo 3
    [37, 44, 31, 85, 51],   # Ciclo 4
    [41, 25, 17, 76, 32],   # Ciclo 5
    [35, 52, 29, 81, 48],   # Ciclo 6
    [29, 68, 45, 88, 65],   # Ciclo 7
    [24, 79, 62, 93, 78],   # Ciclo 8
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional",
]


# ============================================================
# FUNÇÕES DE ANÁLISE POR SENSOR
# ============================================================

def analisar_temperatura(valor):
    """
    Analisa a temperatura interna do módulo (°C).
    Retorna (classificacao, pontuacao, descricao).
    """
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do ideal"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    """
    Analisa a qualidade do sinal de comunicação (%).
    Retorna (classificacao, pontuacao, descricao).
    """
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif valor < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):
    """
    Analisa o nível de bateria da missão (%).
    Retorna (classificacao, pontuacao, descricao).
    """
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):
    """
    Analisa o nível de oxigênio disponível (%).
    Retorna (classificacao, pontuacao, descricao).
    """
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif valor < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):
    """
    Analisa a estabilidade geral dos sistemas (%).
    Retorna (classificacao, pontuacao, descricao).
    """
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif valor < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


# ============================================================
# FUNÇÃO: CALCULAR RISCO DO CICLO
# ============================================================

def calcular_risco_ciclo(ciclo):
    """
    Recebe uma linha da matriz dados_missao e retorna a pontuação
    total de risco do ciclo (0 a 10).
    """
    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

    _, pt, _ = analisar_temperatura(temperatura)
    _, pc, _ = analisar_comunicacao(comunicacao)
    _, pb, _ = analisar_bateria(bateria)
    _, po, _ = analisar_oxigenio(oxigenio)
    _, pe, _ = analisar_estabilidade(estabilidade)

    return pt + pc + pb + po + pe


# ============================================================
# FUNÇÃO: CLASSIFICAR CICLO
# ============================================================

def classificar_ciclo(pontuacao):
    """
    Classifica o ciclo com base na pontuação de risco total.
    0-2  → MISSÃO ESTÁVEL
    3-5  → MISSÃO EM ATENÇÃO
    6-10 → MISSÃO CRÍTICA
    """
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


# ============================================================
# FUNÇÃO: GERAR RECOMENDAÇÃO
# ============================================================

def gerar_recomendacao(ciclo, pontuacao):
    """
    Gera recomendação automática com base nos alertas críticos do ciclo.
    """
    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

    ct, _, _ = analisar_temperatura(temperatura)
    cc, _, _ = analisar_comunicacao(comunicacao)
    cb, _, _ = analisar_bateria(bateria)
    co, _, _ = analisar_oxigenio(oxigenio)
    ce, _, _ = analisar_estabilidade(estabilidade)

    criticos = []
    if ct == "CRÍTICO":
        criticos.append("verificar controle térmico da missão")
    if cc == "CRÍTICO":
        criticos.append("tentar restabelecer contato com a base")
    if cb == "CRÍTICO":
        criticos.append("ativar modo de economia de energia")
    if co == "CRÍTICO":
        criticos.append("acionar protocolo de suporte à vida")
    if ce == "CRÍTICO":
        criticos.append("reduzir operações não essenciais")

    if len(criticos) >= 3:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."
    elif criticos:
        acoes = "; ".join(a.capitalize() for a in criticos)
        return acoes + "."
    elif pontuacao >= 3:
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "Manter operação normal e continuar monitoramento."


# ============================================================
# FUNÇÃO: ANALISAR TENDÊNCIA DA MISSÃO
# ============================================================

def analisar_tendencia(riscos):
    """
    Compara o risco do primeiro ciclo com o do último ciclo.
    Retorna uma string descrevendo a tendência.
    """
    if riscos[-1] > riscos[0]:
        return "A missão apresentou tendência de piora."
    elif riscos[-1] < riscos[0]:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


# ============================================================
# FUNÇÃO: IDENTIFICAR ÁREA MAIS AFETADA
# ============================================================

def identificar_area_mais_afetada(dados):
    """
    Soma a pontuação de risco de cada área ao longo de todos os ciclos
    e retorna o índice e nome da área com maior pontuação acumulada.
    """
    analisadores = [
        analisar_temperatura,
        analisar_comunicacao,
        analisar_bateria,
        analisar_oxigenio,
        analisar_estabilidade,
    ]

    pontuacao_area = [0] * 5

    for ciclo in dados:
        for i, analisar in enumerate(analisadores):
            _, pontos, _ = analisar(ciclo[i])
            pontuacao_area[i] += pontos

    indice_max = pontuacao_area.index(max(pontuacao_area))
    return indice_max, pontuacao_area


# ============================================================
# FUNÇÃO: EXIBIR CICLO NO TERMINAL
# ============================================================

def exibir_ciclo(numero_ciclo, ciclo):
    """
    Exibe no terminal a análise detalhada de um ciclo.
    Retorna a pontuação de risco do ciclo.
    """
    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

    ct, pt, dt = analisar_temperatura(temperatura)
    cc, pc, dc = analisar_comunicacao(comunicacao)
    cb, pb, db = analisar_bateria(bateria)
    co, po, do_ = analisar_oxigenio(oxigenio)
    ce, pe, de = analisar_estabilidade(estabilidade)

    pontuacao = pt + pc + pb + po + pe
    classificacao = classificar_ciclo(pontuacao)
    recomendacao = gerar_recomendacao(ciclo, pontuacao)

    print(f"\nCICLO {numero_ciclo}")
    print("-" * 60)
    print(f"Temperatura:  {temperatura} °C  | {ct:<8} | {dt}")
    print(f"Comunicação:  {comunicacao}%    | {cc:<8} | {dc}")
    print(f"Bateria:      {bateria}%    | {cb:<8} | {db}")
    print(f"Oxigênio:     {oxigenio}%    | {co:<8} | {do_}")
    print(f"Estabilidade: {estabilidade}%    | {ce:<8} | {de}")
    print(f"\nPontuação de risco do ciclo: {pontuacao}")
    print(f"Classificação do ciclo: {classificacao}")
    print(f"Recomendação: {recomendacao}")

    return pontuacao


# ============================================================
# FUNÇÃO: RELATÓRIO FINAL
# ============================================================

def gerar_relatorio_final(dados, riscos):
    """
    Exibe o relatório final consolidado da missão no terminal.
    """
    num_ciclos = len(dados)

    # Médias por sensor
    media_temp  = sum(c[0] for c in dados) / num_ciclos
    media_com   = sum(c[1] for c in dados) / num_ciclos
    media_bat   = sum(c[2] for c in dados) / num_ciclos
    media_oxi   = sum(c[3] for c in dados) / num_ciclos
    media_est   = sum(c[4] for c in dados) / num_ciclos

    # Ciclo mais crítico
    maior_risco = max(riscos)
    ciclo_critico = riscos.index(maior_risco) + 1

    # Risco médio
    risco_medio = sum(riscos) / num_ciclos

    # Ciclos críticos (pontuação >= 6)
    qtd_criticos = sum(1 for r in riscos if r >= 6)

    # Tendência
    tendencia = analisar_tendencia(riscos)

    # Área mais afetada
    idx_area, pontuacao_area = identificar_area_mais_afetada(dados)

    # Classificação final baseada no risco médio
    classificacao_final = classificar_ciclo(round(risco_medio))

    # Conclusão
    if classificacao_final == "MISSÃO CRÍTICA":
        conclusao = (
            "A missão enfrentou situações críticas severas. "
            "É necessária intervenção imediata e revisão completa dos sistemas antes de prosseguir."
        )
    elif classificacao_final == "MISSÃO EM ATENÇÃO":
        conclusao = (
            "A missão apresentou instabilidade relevante durante a operação. "
            "A equipe deve manter o plano de contingência ativo e monitorar os sistemas em atenção."
        )
    else:
        conclusao = (
            "A missão foi concluída com estabilidade satisfatória. "
            "Manter o monitoramento contínuo e registrar os dados para análise posterior."
        )

    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"\nQuantidade de ciclos analisados: {num_ciclos}")
    print(f"\nMédia de temperatura:   {media_temp:.2f} °C")
    print(f"Média de comunicação:   {media_com:.2f}%")
    print(f"Média de bateria:       {media_bat:.2f}%")
    print(f"Média de oxigênio:      {media_oxi:.2f}%")
    print(f"Média de estabilidade:  {media_est:.2f}%")
    print(f"\nCiclo mais crítico:         Ciclo {ciclo_critico}")
    print(f"Maior pontuação de risco:   {maior_risco}")
    print(f"Risco médio da missão:      {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {qtd_criticos}")
    print(f"\nTendência da missão:")
    print(f"  {tendencia}")
    print(f"\nPontuação acumulada por área:")
    for i, area in enumerate(areas_monitoradas):
        print(f"  {area}: {pontuacao_area[i]} pontos")
    print(f"\nÁrea mais afetada:")
    print(f"  {areas_monitoradas[idx_area]}")
    print(f"\nClassificação final da missão:")
    print(f"  {classificacao_final}")
    print(f"\nConclusão:")
    print(f"  {conclusao}")
    print("=" * 60)


# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================

def main():
    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)

    riscos = []

    for i, ciclo in enumerate(dados_missao):
        pontuacao = exibir_ciclo(i + 1, ciclo)
        riscos.append(pontuacao)

    gerar_relatorio_final(dados_missao, riscos)


if __name__ == "__main__":
    main()
