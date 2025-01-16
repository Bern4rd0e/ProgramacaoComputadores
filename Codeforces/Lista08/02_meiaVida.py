tempo, massa = map(int, input().split())


soma = 0

while (massa > 0.5):
    massa = massa / 2
    soma = soma + 1

soma = soma * tempo

seg = 0
min = 0
h = 0
dia = 0

dia = soma // 86400
min = soma % 60

print(dia)
print(soma)
print("{} dias {:02d}:{:02d}:{:02d}".format(dia, h, min, seg))
