def soma(n, m, a = 2, b = 3):
    if a > n or b > m:
        return 0
    else:
        return (a/b) + soma(n, m, a + 1, b + 2)
print("Digite um valor n e um valor m:")
n , m = list(map(int,input().split()))
if n < 0 or m < 0:
    print("Digite dois números positivos!")
resultado = "{:.2f}".format(soma(n,m))
print(resultado)
