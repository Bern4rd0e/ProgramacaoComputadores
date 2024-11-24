pontoInicial = int(input())
pontoFinal = int(input())

largura = 160
altura = 70

areaFelix = ((pontoInicial + pontoFinal) / 2) * altura
areaMarzia = (largura * altura) - areaFelix

if(areaFelix > areaMarzia):
    print(1)
elif(areaMarzia > areaFelix):
    print(2)
else:
    print(0)