# Escreva uma função recursiva que receba uma lista de 
# números inteiros e retorne o índice do maior elemento.
# Assinatura da função: def indice_do_maior(lista)

def indice_do_maior(lista):
    if len(lista) == 0:
        return 0
    else:
        if indice_do_maior(lista[1]) > indice_do_maior(lista[:-1]):
            return indice_do_maior(lista[:1])
        else:
            return indice_do_maior(lista[:-1])

print(indice_do_maior([5, 9, 8]))