jogos = int(input("Digite a quantidade de jogos disputados (1 a 30):  "))


while jogos < 1 or jogos  > 30: 
    print("Quantidade de jogosn invalida")
    jgs = int(input("Digite a quantidade de jogos disputados (1 a 30):  "))

#Caso de numeros maior ou menor do que pedido while retorna a pergunta inicial 

vitória = 0
empate = 0
Derrota = 0
goleadas = 0
gols_pro = 0
gols_contra = 0 
maior_gols_em_um_jogo = 0  


#contador 
contador = 1 

while jogos >= contador:
    print("=== jogo", contador,"===")

#entrada de gols no jogo
gols_marcados = int(input("Quantidade de gols marcados: "))
gols_sofridos = int(input("Quantidade de gols sofridos: "))

if gols_marcados > gols_sofridos


