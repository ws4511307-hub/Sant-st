num1 = int(input( "digite o primeiro numero: "))
num2 = int(input( "digite o segundo numero: "))
operacao = input( "digite a opercao: " )

match operacao: 

    case "+": 
        res = num1 + num2

    case "-": 
        res = num1 - num2

    case "*": 
        res = num1 * num2

    case "/": 
        res = num1 / num2 
print(f"resultado é igual a {res}" )