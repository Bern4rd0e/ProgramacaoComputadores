# Escreva uma função recursiva que receba uma lista de 
# números inteiros e retorne o índice do maior elemento.
# Assinatura da função: def indice_do_maior(lista)

def indice_maior(l):
    if len(l) == 0:
        return 0
    else:
        indiceAtual = l[-1]
        if indiceAtual > indice_maior(l[:-1]):
            return indiceAtual
        else:
            return indice_maior(l[:-1])
print(indice_maior([6,8,9,7,5,10]))
