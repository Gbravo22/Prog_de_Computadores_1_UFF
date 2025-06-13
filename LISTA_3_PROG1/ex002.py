compras = list(map(int,input().split(',')))
a = len(compras)
locaçoes_gratis = []
for i in range(0,a):
    b = compras[i]//10
    locaçoes_gratis.append(b)
print(locaçoes_gratis)
