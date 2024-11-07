diametroBola = int(input())
alturaCaixa, larguraCaixa, profundidadeCaixa = map(int, input().split())

if(diametroBola > alturaCaixa) or (diametroBola > larguraCaixa) or (diametroBola > profundidadeCaixa):
    print("N")
else:
     print("S")
