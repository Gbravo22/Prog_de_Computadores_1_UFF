def sum(a,b):
    resultado = a + b
    print(f"{a} + {b} = {resultado}")
def sub(a,b):
    resultado = a - b
    print(f"{a} - {b} = {resultado}")
def mult(a,b):
    resultado = a * b
    print(f"{a} x {b} = {resultado}")
def div(a,b):
    resultado = a / b
    print(f"{a} : {b} = {resultado}")
def interface_calculadora():
    print("Digite os números que você deseja efetuar a operação:")
    num1 = float(input())
    num2 = float(input())
    print("Digite o número da sua operação:")
    print("1)SOMA")
    print("2)SUBTRAÇÃO")
    print("3)MULTIPLICAÇÃO")
    print("4)DIVISÃO")
    operacao = int(input())
    if operacao == 1:
        sum(num1,num2)
    if operacao == 2:
        sub(num1,num2)
    if operacao == 3:
        mult(num1,num2)
    if operacao == 4:
        if num2 == 0:
            print("Não é permitido divisão por 0")
        else:
            div(num1,num2)
while True:
    print("Quer calcular alguma coisa? [s/n]")
    opcao = input().upper()
    if opcao == "S":
        interface_calculadora()
    if opcao == "N":
        break
