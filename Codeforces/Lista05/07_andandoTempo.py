# a, b, c = map(int, input().split())

# # Inicialmente, assumimos que não é possível retornar ao presente
# resultado = "N"

# # Verificar todas as combinações possíveis
# # Usando apenas um crédito
# if a == 0 or b == 0 or c == 0:
#     resultado = "S"
# # Usando dois créditos
# elif a + b == 0 or a - b == 0 or -a + b == 0 or -a - b == 0:
#     resultado = "S"
# elif a + c == 0 or a - c == 0 or -a + c == 0 or -a - c == 0:
#     resultado = "S"
# elif b + c == 0 or b - c == 0 or -b + c == 0 or -b - c == 0:
#     resultado = "S"
# # Usando os três créditos
# elif a + b + c == 0 or a + b - c == 0 or a - b + c == 0 or a - b - c == 0:
#     resultado = "S"
# elif -a + b + c == 0 or -a + b - c == 0 or -a - b + c == 0 or -a - b - c == 0:
#     resultado = "S"

# # Exibe o resultado
# print(resultado)