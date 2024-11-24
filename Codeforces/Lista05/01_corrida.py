carreta1, distancia1, velocidade1 = map(int, input().split())
carreta2, distancia2, velocidade2 = map(int, input().split())

tempoCarreta1 = distancia1 / velocidade1
tempoCarreta2 = distancia2 / velocidade2

if(tempoCarreta1 > tempoCarreta2):
    print(carreta2)
else:
    print(carreta1)
