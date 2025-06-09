a = int(input("Digite o primeiro número:\n"))
b = int(input("Digite o segundo número:\n"))
c = int(input("Digite o terceiro número:\n"))
soma = a+b+c
media = soma / 3
produto = a*b*c
print(soma)
print(media)
print(produto)
if a > b and a > c:
  print(a)
if b > a and b > c:
  print(b)
if c > a and c > b:
  print(c)
else:
  print("Você digitou 2 ou mais números maiores iguais")
