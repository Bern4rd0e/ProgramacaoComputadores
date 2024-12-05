# Escreva uma função recursiva que receba uma lista de números 
# inteiros e mostre a soma dos números pares
# da lista.
# Assinatura da função: def soma_pares(lista)

def soma_pares(lista):
    if len(lista) == 0:
        return 0
    else:
        ultimo = lista[-1]
        if(ultimo % 2 == 0):
            return 1 + soma_pares(lista[:-1])
        else:
            return 0 + soma_pares(lista[:-1])

print(soma_pares([2,3,3,6,8,5,2]))