nota1, nota2 = map(int, input().split())
peso1, peso2 = map(int, input().split())

peso = (nota1 * peso1) + (nota2 * peso2)

somaPeso = peso1 + peso2

mediaPonderada = int(peso / somaPeso)

print(mediaPonderada)