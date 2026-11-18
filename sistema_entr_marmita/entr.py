import random 
marmitas = ["COSTELA", "OMELETE", "FILE DE FRANGO"]
tamanhos = []
quantidades = []
totais_de_pedidos =[]
lista_precos = []
mais_vendidas = []
#variaveis 
registra_pedido = 1
fechar_o_dia = 2

print("== Cardapio ==")
for i in marmitas:
    print(i)

print("1 - Registra novo pedido")
print("2 - Fechar o dia")
opcão = int(input("Escolha uma opção "))


while opcão != registra_pedido:
      print("1 - Registra novo pedido")
      print("2 - Fechar o dia")
      opcão = int(input("Escolha uma opção valida "))

qnt = int(input("Dígite a quantidade de marmitas(1 a 10): "))

while qnt > 10 or qnt < 0:
    qnt = int(input("Dígite a quantidade de marmitas(1 a 10): "))



if opcão == 1:
  print(">>>> NOVO PEDIDO <<<< ")

contador = 1 

for i in range(qnt):
    print("Tamanho \nP R$15,00 \nM R$18,00 \nG R$22,00")
    tamanho = input(f"Dígite o tamanho da {contador} marmita: ").upper()
    mistura = input("Dígite a mitura: ").upper
    if mistura in marmitas:
        mais_vendidas.append(mistura)
    else:
        print("mistura fora do cardapio")
          mistura = input("Dígite a mitura: ").upper()

    contador = contador + 1

    while tamanho != "P" and tamanho != "M" and tamanho != "G":
       print ("Tamanho invalido dígite um tamanho P M ou G")
       tamanho = input ("Tamanho da marmita P M ou G)").upper()
       mistura = input("Dígite a mitura: ")
       mais_vendidas.append(mistura)
       
    if tamanho == "P":
      preco = 15.00
      lista_precos.append(preco)
   
    elif tamanho == "M":
      preco = 18.00
      lista_precos.append(preco)

    elif tamanho == "G":
      preco = 22.00
      lista_precos.append(preco)



    
print(mais_vendidas)
print(tamanhos)
print(quantidades)
print(lista_precos)