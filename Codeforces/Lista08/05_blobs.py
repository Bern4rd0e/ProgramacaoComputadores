testes = int(input()) 

for i in range(testes):
    valor = float(input())  

    cont = 0 

    while valor > 1.0:
        valor = valor / 2  
        cont += 1 

    print(f"{cont} dias")