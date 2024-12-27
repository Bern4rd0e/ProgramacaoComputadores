n = int(input())


if n == 1:
    print('Nao')
else:
    cont = 0

    for i in range(2, n + 1):
        if n % i == 0:
            cont += 1
        
    if cont > 1:
        print('Nao')
    else:
        print('Sim')

