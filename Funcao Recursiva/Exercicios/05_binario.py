# Escreva uma função recursiva que determine quantos bits 
# são necessários para representar um determinado
# número, ignorando os zeros a esquerda.
# Exemplo: Para o número 4312 são necessários 13 bits, 
# pois 4312(10) = 1000011011000(2)
# Assinatura da função: def conta_bits(n)


def conta_algarismos(n):
    if n == 0:
        return 0
    else:
        return 1 + conta_algarismos(n // 2)

print(conta_algarismos(4312))