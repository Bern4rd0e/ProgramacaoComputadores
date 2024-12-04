# Escreva uma função recursiva que receba um inteiro n, 
# não negativo, e retorne a quantidade de divisores de n. 
# Assinatura da função: def conta_divisores(n)

def divisores(a, b):
    if b == 1:
        return 1
    else:
        if a % b == 0:
            return 1 + divisores(a, b-1)
        else: 
            return 0 + divisores(a, b-1)

def conta_divisores(n):
    return divisores(n, n) 
        
print(conta_divisores(10))