# Escreva uma função recursiva que determine se os elementos de uma 
# lista estão ordenados. A função deve
# retornar um valor lógico (boolean).
#  Em Python os possíveis valores lógicos são True ou False.
# Assinatura da função: def ordenada(lista)

def lista_ordenada(l):
    if len(l) < 2:
        return True
    else:
        if l[0] <= l[1]:
            return lista_ordenada(l[:-1]) 
        else:
            return False
        

print(lista_ordenada([7,9,9,10]))