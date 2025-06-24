def media(a,b,c):
    soma = a + b + c
    return soma/3
def suavizar(funcao, lista, i = 0):
    final = len(lista) - 1
    listamedia = []
    listamedia.append(lista[0])
    for j in range(1, final - 1):
        listamedia.append(funcao(lista[j - 1],lista[j],lista[j + 1]))
    listamedia.append(lista[final - 1])
    listamedia.append(lista[final])
    return listamedia
print("Digite sua lista")
lista = list(map(int, input().split()))
L = list(suavizar(media, lista))
print(L)
