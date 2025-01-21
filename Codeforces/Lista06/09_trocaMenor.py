def lista_troca_menor_primeiro(lista):
    if not lista:
        return 0

    indice_menor = lista.index(min(lista))

    if indice_menor == 0:
        return 0
    else:
        lista[0], lista[indice_menor] = lista[indice_menor], lista[0]
        print(1)
        return lista 

# Testando a função
print(lista_troca_menor_primeiro([2, 4, 6, 8, 1, 3, 5, 7]))  # Deve retornar 1 e imprimir a lista com a troca
