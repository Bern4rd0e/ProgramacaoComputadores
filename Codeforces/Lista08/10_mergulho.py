voluntarios, retornoMergulho = map(int, input().split())
retornaram = list(map(int, input().split()))

for i in range(1, voluntarios + 1):
    if i not in retornaram:
        print(i, end=" ")


if all(i in retornaram for i in range(1, voluntarios + 1)):
    print("*")