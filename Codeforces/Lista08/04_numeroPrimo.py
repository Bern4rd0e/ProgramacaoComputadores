def is_prime(x):
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    # Verifica divisibilidade de 5 até x-1
    for i in range(5, x):
        if x % i == 0:
            return False
    return True

# Leitura da entrada
n = int(input())

# Encontrar o menor número primo maior que n
p = n + 1
while not is_prime(p):
    p += 1

# Imprimir o resultado
print(p)
