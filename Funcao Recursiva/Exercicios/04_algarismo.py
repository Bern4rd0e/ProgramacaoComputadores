# Escreva ma função recursiva que determine quantos algarismos 
# são necessários para representar um determinado
# número, ignorando os zeros a esquerda.
# Exemplo: Para o número 12345 são necessários 5 algarismos, pois
# Assinatura da função: def conta_algarismos(n)

def conta_algarismos(n):
    n = abs(n)
    if n == 1 or n == 0:
        return 1
    else:
        return 1 + conta_algarismos(n // 10)


def soma_digitos(n):
    n = abs(n)

    if n == 0:
        return 0
    else:
        return (n % 10) + soma_digitos(n // 10)

print(conta_algarismos(0))
print(soma_digitos(123))


