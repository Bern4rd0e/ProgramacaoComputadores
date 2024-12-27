lista01 = list(map(int, input().split()))
lista02 = list(map(int, input().split()))

valoresIguais = list(set(lista01) & set(lista02))

if valoresIguais:
    print(valoresIguais)
else:
    print("Sem valores iguais")