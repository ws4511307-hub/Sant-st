'''
# Exe.1 Carro multado?
vel = float(input("Qual a velociade do carro? "))
vl_mx = 80 
print("O carro foi multado?", vel >= vl_mx)
'''
'''
# Exe.2 Compra permitida?
comp = float(input('Qual valor da sua compra? '))
saldo = 500 
r = comp <= saldo 
print("Compra permitida? ", r)
'''
'''
# Exe.3 Saldo suficiente
saldo_atual = float(input("Qual saldo atual? "))
val_com = float(input("Valor da sua compra? "))
r = saldo_atual - val_com
print("Saldo restante: ", r)
input("Saldo suficiente?" ) 
print(r >= 0)
'''
'''
# Exe.4 metas de venda 
Qnt_prod_m = int (input("Qual a quantidade de produtos da manha?: ")) 
Qnt_prod_t = int (input("Qual a quantidade de produtos da tarde? "))
meta_d = 100
print(Qnt_prod_m >= meta_d, Qnt_prod_t >= meta_d)
'''
'''
prod1 = int (input(" Digite o valor do produto 1?: "))
prod2 = int (input("Digite o valro do produto 2?: "))
frt_gts = 150
f = input("frete gratis?") 
r = prod1 >= frt_gts, prod2 >= frt_gts
print( f, r)
''' 
'''
num = int(input("Digite um numero: "))

if num > 0: 
    print("O numero é positivo ")

else: 
    print("O numero é nagativo")
    '''
'''
idade = int(input("Digite sua idade: "))

if idade > 18:
    print("Você é de maior")


else:
    print("você é de menor")
 '''   
'''
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 > num2:
    print("O primeiro numero é maior")

else:
    print("O segundo numero é maior")
'''
'''
notaf = float(input("Digite a nota: "))

if notaf > 6:
    print("Aluno aprovado")

else:
    print("Aluno reprovado")
    '''
'''
prod = int(input("Quantidade de produtos em estoque:"))

if prod >= 10:
    print("Estoque suficiente ")

else:
    print("Estoque baixo")
    '''
'''
num_int = int(input("Digite um numero: ")) 

if num_int % 2 == 0:
    print("Numero par")


else: 
    print("numero impar")
    '''
'''
temp = int(input("Qual a temperatura: "))

if temp >= 30:
    print("Esta quante")

else:
    print("Esta frio")
    '''
''' 
x =  int(input("Qual o valor de x? "))
y =  int(input("Qual o valor de y? "))
z =  int(input("Qual o valor de z? "))

if x == 1 and y == 2 and z == 3:
    print(f"Entrou na opção {x, y, z}")
else :
    print("Saio do menu")
'''
'''
possui_cupom = int(input("Digite o cumpom: "))
cumpom = 5634
eh_vip = int(input("digite seu cod vip: "))
 
if possui_cupom == cumpom or eh_vip == 5437:
    print("Desconto de 20% ")

else:
    print("Não possui desconto")

    '''
'''
x = int(input("Digite o primeiro numero: ")) 
y =  int(input("Digite o segundo numero"))

if x >= 5:
 if y <= 15:
    print(" opção a ")
 else:
        print("opção b")

else:
    print(" opção c ")

'''

'''
x = int(input("Digite o primeiro numero: ")) 
y =  int(input("Digite o segundo numero"))

if x >= 5 and y <= 15:
    print("Opção a")
 
else:
    print("Opção b ")

'''


"""
nome = "ana" 
idade = 17 

print(f" óla, me chamo {nome} e tenho {idade} anos")
""" 
'''
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

print(f"Seja bem vindo(a) {nome} sua iadede é {idade}")
'''
'''
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
cnh = int(input("Digite o numero da sua cnh: "))

if idade >= 18 and cnh == 7425: 
    print(f"Óla {nome}, você pode dirigir!!! ")

else:
    print(f"Óla {nome}, você não pode dirigir")
'''

'''
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
cnh = int(input("Digite o numero da sua cnh: "))

if idade >= 18 and cnh == 7425: 
    print(f"Óla {nome}, você pode dirigir!!! ")

elif idade < 18:
    print(f"Óla {nome}, você não pode dirir é menor da idade")

else:
    print(f"Óla {nome}, você não pode dirigir cnh invalida")

'''
'''
print(f"O dobro de 5 é {5*2}")
'''

# caixa super mercado 

produto = input("Digite o produto: ")
preço = float(input("Digite o preço: R$ "))
quantidade = int(input("Digite a quantidade de peodutos: "))

subtotal = preço * quantidade

if subtotal >= 100:
    desconto = subtotal  * 0.10

else:
    desconto = 0 

total = subtotal - desconto

print(f"Produto: {produto}")
print(f"subtotal: R$ {subtotal: .2f}")
print(f"desconto: {desconto: .2f}")
print(f"total: {total: .2f} ")