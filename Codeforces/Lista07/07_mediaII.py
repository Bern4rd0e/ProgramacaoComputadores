qtd = int(input())

numeros = list(map(int, input().split()))


media = sum(numeros) / len(numeros)
print("{:.1f}".format(media))

def menor(lista, media):
    contador = 0
    for num in lista:
        if num < media:
            contador += 1
    print(contador, end=' ')
    for num in lista:
        if num < media:
            print(num, end=' ')
    print()
    return contador


menor(numeros, media)

def maior(lista, media):
    contador = 0
    for num in lista:
        if num >= media:
            contador += 1
    print(contador, end=' ')
    for num in lista:
        if num >= media:
            print(num, end=' ')
    print() 
    return contador

maior(numeros, media)

# N = int(input())

# # Lê a lista de números inteiros
# numeros = list(map(int, input().split()))

# # Calcula a média
# media = sum(numeros) / N

# # Imprime a média com 1 casa decimal
# print(f"{media:.1f}")

# # Listas para armazenar os números abaixo e acima (ou igual) à média
# abaixo = []
# acima_ou_igual = []

# # Separa os números conforme a média
# for num in numeros:
#     if num < media:
#         abaixo.append(num)
#     else:
#         acima_ou_igual.append(num)

# # Imprime a quantidade de números abaixo da média e os números
# print(len(abaixo), *abaixo)

# # Imprime a quantidade de números acima ou igual à média e os números
# print(len(acima_ou_igual), *acima_ou_igual)