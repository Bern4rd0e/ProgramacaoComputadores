teste = int(input())

for i in range(teste):
    quantia, marcas = map(int, input().split())
    preco = list(map(float, input().split()))

    troco = 0
    
    for i in list(preco):
        if quantia%i > troco and quantia%i != quantia:
            troco = quantia%i

    print("{:.2f}".format(troco))


    

