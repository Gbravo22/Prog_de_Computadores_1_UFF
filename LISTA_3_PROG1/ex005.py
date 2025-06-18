print("Digite os elementos da primeira lista")
lista_n = list(map(int,input().split()))
print("Digite os elementos da segunda lista:")
lista_m = list(map(int,input().split()))
if len(lista_m) > len(lista_n):
    lista_maior = lista_m
    lista_menor = lista_n
else:
    lista_maior = lista_n
    lista_menor = lista_m
lista_mesclada = []
for i in range(0,len(lista_menor)):
    lista_mesclada.append(lista_menor[i])
    lista_mesclada.append(lista_maior[i])
for j in range(len(lista_menor),len(lista_maior)):
    lista_mesclada.append(lista_maior[j])
print(lista_mesclada)
