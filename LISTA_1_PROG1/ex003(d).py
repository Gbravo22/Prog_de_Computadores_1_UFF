a = int(input("Digite aqui o número a:\n"))
b = int(input("Digite aqui o número b:\n"))
c = int(input("Digite aqui o número c:\n"))
if a == b and b ==c:
  print(0)
elif a == b and c!=b:
  print(c)
elif a == c and b!= c:
  print(b)
elif b == c and a!=b:
  print(a)
else:
  print(a+b+c)
  
