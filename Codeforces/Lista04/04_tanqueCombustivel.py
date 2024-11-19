consumo = int(input())
distancia = int(input())
combustivel = int(input())

consumoTotal = distancia / consumo
combustivelFalta = "{:.1f}".format(consumoTotal - combustivel)

if(consumoTotal > combustivel):
    print(combustivelFalta)
else:
    print(0.0)