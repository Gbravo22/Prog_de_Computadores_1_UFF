def fibonacci_menor_que_L():
    while True:
        try:
            L = int(input("Digite o valor limite (L): "))
            if L <= 0:
                print("Por favor, digite um número inteiro positivo para L.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    print(f"\nTermos de Fibonacci menores que {L}:")
    termo1 = 1
    if termo1 < L:
        print(termo1)
    termo2 = 1
    if termo2 < L:
        print(termo2)
    while (termo1 + termo2) < L:
        novo_termo = termo1 + termo2
        print(novo_termo)
        termo1 = termo2
        termo2 = novo_termo
fibonacci_menor_que_L()
