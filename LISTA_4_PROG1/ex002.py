def verif_sequenc(lista, i=0, sequencia_atual=1, maior_sequencia=1):
    if i == len(lista) - 1:
        return max(maior_sequencia, sequencia_atual)
    else:
        if lista[i] < lista[i+1]:
            return verif_sequenc(lista, i + 1, sequencia_atual + 1, maior_sequencia)
        else:
            return verif_sequenc(lista, i + 1, 1, max(maior_sequencia, sequencia_atual))
lista1 = list(map(int, input().split()))
if not lista1:
    a = 0
else:
    a = verif_sequenc(lista1)
print(a)
