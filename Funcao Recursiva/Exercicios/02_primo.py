# Escreva uma função recursiva que receba um número inteiro, 
# não negativo, e retorne se ele é primo.
# Assinatura da função: def primo(n)

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
        return "é primo"
    else:
        return "não é primo"
        
print(primo(5))