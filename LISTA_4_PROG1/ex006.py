def lista_tribonacci(n):
    lista = []
    a = 1
    b = 1
    c = 2
    d = 0
    lista.append(a)
    lista.append(b)
    lista.append(c)
    return tribonacci(lista,a,b,c,d,n)
def tribonacci(lista,a,b,c,d,n):
        d = a + b + c
        a = b
        b = c
        c = d
        if c > n:
              return lista
        else:
            lista.append(c)
            return tribonacci(lista,a,b,c,d,n)
print("Digite o n:")
n = int(input())
l = lista_tribonacci(n)
print(l)
