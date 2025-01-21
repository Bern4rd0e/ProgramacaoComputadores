pulo, cano = map(int, input().split())
alturas = list(map(int, input().split()))

for i in range(1, cano):
    # abs retorna o valor positivo ao invés de negativo
    if abs(alturas[i] - alturas[i-1]) > pulo:
        print("GAME OVER")
        break
else:
    print("YOU WIN")

