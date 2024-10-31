distancia = int(input())
velocidade = int(input())

tempoGasto = 60 * distancia // velocidade

horas = tempoGasto // 60
minutos = tempoGasto % 60

print("{:02d}".format(horas), "{:02d}".format(minutos), sep=":")