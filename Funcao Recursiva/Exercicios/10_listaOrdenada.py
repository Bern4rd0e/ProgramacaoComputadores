# Escreva uma função recursiva que determine se os elementos de uma 
# lista estão ordenados. A função deve
# retornar um valor lógico (boolean).
#  Em Python os possíveis valores lógicos são True ou False.
# Assinatura da função: def ordenada(lista)

def lista_ordenada(l):
    if len(l) < 2:
        return True
    else:
        if l[-1] > l[-2]:
            return True
        else:
            return False
        

print(lista_ordenada([7,8,9,10]))