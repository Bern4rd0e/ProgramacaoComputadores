comprimentoEstrada, distancia = map(int, input().split())
valorQuilometro, valorPedagio = map(int, input().split())

pedagios = comprimentoEstrada // distancia * valorPedagio

valoraKm = comprimentoEstrada * valorQuilometro

valorTotal = valoraKm + pedagios

print(valorTotal)
