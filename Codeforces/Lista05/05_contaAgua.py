consumo = int(input())

if consumo <= 10:
    custo = 7
elif consumo <= 30:
    custo = 7 + (consumo - 10) * 1
elif consumo <= 100:
    custo = 7 + 20 + (consumo - 30) * 2
else:
    custo = 7 + 20 + 140 + (consumo - 100) * 5

print(custo)