def bubblesort(lista):
    for i in range(0,len(lista)):
        for j in range(0,len(lista) - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
lista_telefones = []
while True:
    print("Digite o número(0 para encerrar o programa)")
    numero = int(input())
    if numero == 0:
        print(lista_telefones)
        break
    else:
        lista_telefones.append(numero)
        print(bubblesort(lista_telefones))
