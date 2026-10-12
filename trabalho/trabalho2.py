#sistema de time de varzea

#wemerson 
jg = int(input("Digite a quantidade de jogos disputado (0 a 30): "))

# Enquanto o número for menor que 0 OU maior que 30, o Python vai repetir
while jg < 0 or jg > 30:
    print("Quantidade de jogos invalida!!")
    jg = int(input("Digite a quantidade de jogos (0 a 30): "))

#tabela de resumo da campanha, que vai ser apresentada no final.
vitorias = 0
empates = 0
derrotas = 0
goleadas = 0
gols_pro = 0
gols_contra = 0
maior_gols_em_um_jogo = 0


#Contador para o laço de repetição
#/n = quebra de linha "pula linha no meio de um srting"
contador = 1


while contador <= jg:
    print("\n--- JOGO", contador, "---")

#entradas de gols 

gols_sofridos = int(input("Quantidade de gols sofrido: "))
gols_marcados = int(input("Quantidade de gols marcados: "))
    
contador = contador + 1