lista = list(map(float, input().split()))
elementos = len(lista) 
limite = elementos - 1
menor = 10000
numero_desejado = 0
def soma(lista, i = 0):
    if i > limite:
        return 0
    if i <= limite:
        return lista[i] + soma(lista, i + 1)
media = (soma(lista))/elementos
for i in range(0,elementos):
    diferença = abs(lista[i] - media)
    if diferença < menor:
        menor = diferença
        numero_desejado = lista[i]
    else:
        continue
print(media)
print(numero_desejado)
