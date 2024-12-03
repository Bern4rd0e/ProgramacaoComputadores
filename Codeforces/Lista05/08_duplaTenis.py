A = int(input())
B = int(input())
C = int(input())
D = int(input())

# Calcular as três possíveis diferenças
diferenca1 = abs((A + B) - (C + D))
diferenca2 = abs((A + C) - (B + D))
diferenca3 = abs((A + D) - (B + C))

# Determinar a menor diferença entre as três
menor_diferenca = diferenca1

if diferenca2 < menor_diferenca:
    menor_diferenca = diferenca2

if diferenca3 < menor_diferenca:
    menor_diferenca = diferenca3

# Exibir a menor diferença
print(menor_diferenca)