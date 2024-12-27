qtd = int(input())

numeros = list(map(int, input().split()))


media = sum(numeros) / len(numeros)
print("{:.1f}".format(media))

def menor(lista, media):
    contador = 0
    for num in lista:
        if num < media:
            contador += 1
    return contador

print(menor(numeros, media))

def maior(lista, media):
    contador = 0
    for num in lista:
        if num >= media:
            contador += 1
    return contador

print(maior(numeros, media))


# def menor(lista):
#     if len(lista) == 0:
#         return 0
#     else:
#         if lista < media:
#             return 1 + menor(lista[-1])
#         else:
#             return 0 + menor(lista[-1])