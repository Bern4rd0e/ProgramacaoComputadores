# Escreva uma função recursiva que receba uma lista l1 de números 
# inteiros e retorne uma outra lista l2 com os
# números primos de l1.
# Assinatura da função: def primos(lista)
# Obs: Use a função primo(), feita anteriormente, 
# para determinar se um número é primo.

def divisores(a, b):
    if b == 1:
        return 1
    else:
        if(a % b == 0):
            return 1 + divisores(a, b - 1)
        else:
            return 0 + divisores(a, b - 1)

def primo(n):
    if divisores(n, n) == 2:
        return n
    else:
        return "não é primo"
        
def primos(l):
    if len(l) == 0: 
        return 0
    else:
        return primo(l[-1]) 
        
print(primos([2,7,5,6,4,3]))