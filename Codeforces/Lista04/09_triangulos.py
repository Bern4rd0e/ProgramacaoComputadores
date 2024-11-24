a, b, c = map(int, input().split())

if a >= b and a >= c:
    maior = a
    lado1 = b
    lado2 = c
elif b >= a and b >= c:
    maior = b
    lado1 = a
    lado2 = c
else:
    maior = c
    lado1 = a
    lado2 = b

if (lado1 + lado2 > maior) and (lado1 + maior > lado2) and (lado2 + maior > lado1):
    # Verificar o tipo de triângulo
    if maior**2 == lado1**2 + lado2**2:  # Triângulo retângulo
        print("r")
    elif maior**2 < lado1**2 + lado2**2:  # Triângulo acutângulo
        print("a")
    else:  # Triângulo obtusângulo
        print("o")
else:
    print("n") 