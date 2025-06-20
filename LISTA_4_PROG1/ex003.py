def alterar(c):
    if c < 10:
        if c < 0:
            return 0
        else:
            return 1
    else:
        return 2
print("Quantos números você quer colocar na lista?")
n = int(input())
lista_original = []
for i in range(0,n):
    print("Digite um número para colocar na lista:")
    a = int(input())
    lista_original.append(a)
lista_alterada = list(map(alterar,lista_original))
print(lista_alterada)
