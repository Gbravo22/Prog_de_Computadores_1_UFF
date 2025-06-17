def calcular_estatisticas():
    n = 0
    while not (1 <= n <= 30):
        n = int(input("Quantos números inteiros você deseja inserir (entre 1 e 30)? "))
        if not (1 <= n <= 30):
            print("Por favor, insira um número entre 1 e 30.")
    numeros = []
    for i in range(n):
        num = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(num)
    soma = sum(numeros)
    media = soma / n
    produto = 1
    for num in numeros:
        produto *= num
    menor_valor = numeros[0]
    for num in numeros:
        if num < menor_valor:
            menor_valor = num
    maior_valor = numeros[0]
    for num in numeros:
        if num > maior_valor:
            maior_valor = num
    print("\n--- Resultados ---")
    print(f"Números inseridos: {numeros}")
    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")
    print(f"Produto: {produto}")
    print(f"Menor valor: {menor_valor}")
    print(f"Maior valor: {maior_valor}")
if __name__ == "__main__":
    calcular_estatisticas()
