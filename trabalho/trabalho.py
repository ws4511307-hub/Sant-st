# === SISTEMA DE TIME DE VÁRZEA COMPLETO ===

jogos = int(input("Digite a quantidade de jogos disputados (0 a 30): "))

# Variáveis para guardar o resumo da campanha
vitorias = 0
empates = 0
derrotas = 0
goleadas = 0
gols_pro = 0
gols_contra = 0
maior_gols_em_um_jogo = 0

# Contador para o laço de repetição
contador = 1
while contador <= jogos:
    print("\n--- JOGO", contador, "---")
    
    # Entrada de gols do jogo
    gols_marcados = int(input("Gols que seu time MARCOU: "))
    gols_sofridos = int(input("Gols que seu time SOFREU: "))
    
    # Acumula o total de gols
    gols_pro = gols_pro + gols_marcados
    gols_contra = gols_contra + gols_sofridos
    
    # Verifica qual foi o maior número de gols em uma única partida
    if gols_marcados > maior_gols_em_um_jogo:
        maior_gols_em_um_jogo = gols_marcados
    
    # Descobre o resultado do jogo e conta pontos/vitorias/empates/derrotas
    if gols_marcados > gols_sofridos:
        resultado = "Vitória"
        vitorias = vitorias + 1
    elif gols_marcados == gols_sofridos:
        resultado = "Empate"
        empates = empates + 1
    else:
        resultado = "Derrota"
        derrotas = derrotas + 1
        
    # Mostra o resultado deste jogo específico
    print("Resultado do Jogo", contador, ":", resultado, "por", gols_marcados, "x", gols_sofridos)
    
    # Verifica se foi goleada (considerando 4 ou mais gols de vantagem)
    if (gols_marcados - gols_sofridos) >= 4:
        print("🔥 AVISO: Isso foi uma GOLEADA a favor do seu time!")
        goleadas = goleadas + 1
        
    # Passa para o próximo jogo
    contador = contador + 1

# --- CÁLCULOS FINAIS DA CAMPANHA ---
pontos_ganhos = (vitorias * 3) + (empates * 1)
pontos_maximos = jogos * 3
saldo_gols = gols_pro - gols_contra

# Calcula a média de gols (evita erro se jogos for zero)
if jogos > 0:
    media_gols = gols_pro / jogos
    aproveitamento = (pontos_ganhos / pontos_maximos) * 100
else:
    media_gols = 0
    aproveitamento = 0

# Tabela de situação
if aproveitamento >= 70:
    situacao = "Briga pelo título"
elif aproveitamento >= 50:
    situacao = "Zona de classificação"
elif aproveitamento >= 30:
    situacao = "Meio da tabela"
else:
    situacao = "Risco de rebaixamento"

# --- RELATÓRIO DO CAMPEONATO ---
print("\n==========================================")
print("         RESUMO DA CAMPANHA DO TIME       ")
print("==========================================")
print("Pontos Conquistados:         ", pontos_ganhos)
print("Vitórias:                    ", vitorias)
print("Empates:                     ", empates)
print("Derrotas:                    ", derrotas)
print("Goleadas Aplicadas:          ", goleadas)
print("Gols Pró (Marcados):         ", gols_pro)
print("Gols Contra (Sofridos):      ", gols_contra)
print("Saldo de Gols:               ", saldo_gols)
print("Média de Gols por Jogo:      ", media_gols)
print("Maior nº de Gols em um Jogo: ", maior_gols_em_um_jogo)
print("Aproveitamento:              ", aproveitamento, "%")
print("Situação Atual:              ", situacao)
print("==========================================")
