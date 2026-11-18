import secrets 
import string

def Gerar_senha_segura(comprimento = 12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = " " . join(secrets.choice(caracteres) for i in range(comprimento))
    return senha 

senha_segura = Gerar_senha_segura(16)
print(f"Senha segura gerada é:  {senha_segura}")

senha = input("Digite sua senha: ")

if senha_segura == senha:
    print("Acesso permitido")

else:
    print("acesso negado")