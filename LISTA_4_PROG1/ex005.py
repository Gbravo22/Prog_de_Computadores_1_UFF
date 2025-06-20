def indice_min(lista, k):
    elementos = len(lista) - 1
    parametro = lista[k]
    elemento = lista[k]
    for i in range(k,elementos):
        if lista[i] < parametro:
            parametro = i
            elemento = lista[i]
        else:
            continue
    return parametro, elemento
print("Digite os elementos da sua lista, separados por vírgulas:")
lista = list(map(int,input().split(",")))
print("Digite agora o parâmetro K:")
k = int(input())
parametro, elemento = (indice_min(lista, k))
print(f"O menor número após o parâmetro K é {elemento}, cuja posição é {parametro}")
