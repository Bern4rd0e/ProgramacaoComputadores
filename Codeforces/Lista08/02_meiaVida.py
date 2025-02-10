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
# Aqui remove os segundos já convertidos para dias
soma %= 86400
h = soma // 3600
# Aqui remove os segundos já convertidos para horas
soma %= 3600
min = soma // 60
# Aqui obtém o restante (segundos)
seg = soma % 60



print("{} dias {:02d}:{:02d}:{:02d}".format(dia, h, min, seg))