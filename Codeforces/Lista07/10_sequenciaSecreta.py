# # Leitura do tamanho da sequência
# N = int(input())

# # Leitura da sequência de números
# sequencia = [int(input()) for _ in range(N)]

# # Variável para contar o número máximo de marcas
# marcados = 1  # Sempre marcamos o primeiro número, que é 1
# ultimo = sequencia[0]  # O primeiro número é 1

# # Percorre o restante da sequência
# for i in range(1, N):
#     if sequencia[i] != ultimo:  # Se for diferente do último marcado
#         marcados += 1
#         ultimo = sequencia[i]  # Atualiza o último número marcado

# # Imprime a quantidade máxima de números marcados
# print(marcados)
