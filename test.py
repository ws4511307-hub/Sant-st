
jogos = int(input("Quantidade de jogos disputados( 1 a 30): "))

while jogos < 1 or jogos >= 31:
    print("Quantidade invalida")
    int(input("Quantidade de jogos disputados( 1 a 30): "))

#variaveis 
vitoria = 0 
empate = 0
derrota = 0
gols_pro = 0 
gols_contra = 0
goleada = 0
total_de_pontos = 0

contador = 1 

while jogos >= contador:
    print("    === registro de jogo", contador,"===")
    gols_marcados = int(input("Digite a quantidades de gols marcados: "))
    gols_sofridos = int(input("Digite a quantidade de gols sofridos: "))


    if gols_marcados > gols_sofridos:
        if gols_marcados > 3:
            print(" Goleadaaa!!!") 
            goleada = goleada + 1
        print(" Resultado: vitoria \n")
        total_de_pontos = total_de_pontos + 3 
        vitoria = vitoria + 1
        gols_pro = gols_pro + gols_marcados
        gols_contra = gols_contra + gols_sofridos
        

    elif gols_sofridos == gols_marcados:
        print("Resultado: empate \n" )
        total_de_pontos = total_de_pontos +1
        empate = empate + 1 
        gols_pro = gols_pro + gols_marcados
        gols_contra = gols_contra + gols_sofridos

    elif gols_marcados < gols_sofridos:
        print("Resultado: derrota \n" ) 
        total_de_pontos = total_de_pontos + 0 
        derrota = derrota + 1
        gols_pro = gols_pro + gols_sofridos
        gols_contra =  gols_contra + gols_sofridos

    contador = contador + 1 



print("   >>>> RESUMO DA CAMPANHA <<<<<< \n")

print("Quantidade de vitorias:", vitoria )
print("Quantidade de empates:", empate)
print("Quantidade de derrots:", derrota)
print("gols marcados:", gols_pro)
print( "gols sofridos:", gols_contra)
print("goleadas:", goleada)
print ("pontos:",total_de_pontos)

aproveitamento = (total_de_pontos /  (jogos * 3)) * 100

if aproveitamento >= 70:
    print("Situação: Briga pelo titulo")

elif aproveitamento >= 50:
    print("Situação: zona de clasificação")

elif aproveitamento >= 30:
    print("Situação: meio da tabela")

else:
    print("Situação: risco de rebaixamento")

#fim 