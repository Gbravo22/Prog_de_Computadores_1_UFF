def bubblesort_reverse(lista_med,lista_nom,i = 0):
    for i in range(0,len(lista_med)):
        for j in range(0,len(lista_med) - i - 1):
            if lista_med[j] < lista_med[j+1]:
                lista_med[j],lista_med[j+1] = lista_med[j+1], lista_med[j]
                lista_nom[j],lista_nom[j+1] = lista_nom[j+1], lista_nom[j]
    return lista_med, lista_nom
print("Digite o número de candidatos:")
n_candidatos = int(input())
lista_nomes = []
lista_medias = []
for i in range(0,n_candidatos):
    print("Digite o nome do candidato acompanhado de suas 3 notas:")
    nome, a, b, c = list(input().split())
    a, b, c = int(a), int(b), int(c)
    media = (a+b+c)/3
    lista_nomes.append(nome)
    lista_medias.append(media)
lista_med_ordenada , lista_nomes_ordenada = bubblesort_reverse(lista_medias,lista_nomes)
print("Você deseja ver qual opção?")
print("1) lista dos melhores candidatos")
print("2) lista das melhores médias")
print("3) ver as duas listas")
escolha = int(input())
if escolha == 1:
    print(lista_nomes_ordenada)
if escolha == 2:
    print(lista_med_ordenada)
if escolha == 3:
    print(lista_med_ordenada)
    print(lista_nomes_ordenada)
else:
    print("Escolha um número válido")
