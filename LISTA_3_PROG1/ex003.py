lista = list(map(int,input().split()))
tamanho = len(lista)
limite = tamanho - 1
l_invertida = []
l_fatorial = []
def inverter(lista, i = limite):
    if i < 0:
        return l_invertida
    if i >= 0:
        l_invertida.append(lista[i])
        return inverter(lista, i - 1)
def fatorial(numero):
    if numero == 1:
        return 1
    if numero > 1:
        return numero*fatorial(numero-1)
print(inverter(lista))
print(list(map(fatorial,lista)))
