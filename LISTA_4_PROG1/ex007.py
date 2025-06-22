print("Digite a palavra que deseja verificar:")
palavra = str(input())
def eh_palindrome(palavra, verificar = True, inicio = 0, fim = len(palavra) - 1):
    if len(palavra) == 0:
        return True
    if inicio == fim:
        return verificar
    else:
        if palavra[inicio] == palavra[fim]:
            return eh_palindrome(palavra, verificar = True, inicio = inicio + 1, fim = fim - 1)
        else:
            return False
verificacao = eh_palindrome(palavra)
print(verificacao)
