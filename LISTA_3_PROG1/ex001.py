lista = []
def colocarlista(a):
    lista.append(a)
    return lista
for i in range(0,5):
    colocarlista(input('Insira aqui um número:\n'))
vetor = input('Digite o número a ser verificado: ')
if vetor in lista:
    i = 0
    while i<=len(lista):
        if vetor == lista[i]:
            print(f'Esse vetor está dentro da lista e está na posição {i+1}')
            break
        else:
            i = i +1
else: 
    print('Esse vetor que você digitou não está dentro da lista')
