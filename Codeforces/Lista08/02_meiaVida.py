tempo, massa = map(int, input().split())

soma = 0

while (massa > 0.5):
    massa = massa / 2
    # print(massa)
    soma = soma + 1

soma = soma * tempo

seg = 0
min = 0
h = 0
dia = 0

if soma < 60:
    seg = soma
    print("{} dias {:02d}:{:02d}:{:02d}".format(dia, h, min, seg))
elif soma >= 60:
    min = soma
    seg = int(min % 60)
    min = int(min / 60)
    print("{} dias {:02d}:{:02d}:{:02d}".format(dia, h, min, seg))
    if min > 60:
        seg = int(min % 60)
        min = int(min / 60)
        h = int(min % 60)
        print("{} dias {:02d}:{:02d}:{:02d}".format(dia, h, min, seg))
