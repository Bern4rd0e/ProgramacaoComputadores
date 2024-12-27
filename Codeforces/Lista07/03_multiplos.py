a, b = map(int, input().split())


multiplos = []

for i in range(1,b + 1):
    if a * i <= b:
        multiplos.append(a * i)

print(*multiplos)