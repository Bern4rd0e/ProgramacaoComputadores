a1 = int(input())
a2 = int(input())
a3 = int(input())

# if(a1 > a2) and (a1 > a3):
#     if(a2 > a3):
#         print(a1 * 0 + a2 * 2 + a3 * 4)
#     else:
#         print(a1 * 0 + a3 * 4 + a2 * 2)
# elif(a2 > a3):
#     if(a1 > a3):
#         print(a2 * 0 + a1 * 2 + a3 * 2)
#     else:
#         print(a2 * 0 + a3 * 2 + a1 * 2)
# else:
#     if(a1 > a2):
#         print(a3 * 0 + a1 * 4 + a2 * 2)
#     else:
#         print(a3 * 0 + a2 * 2 + a1 * 4)


# Cálculo do tempo gasto para cada posicionamento da máquina
tempo1 = a1 * 0 + a2 * 2 + a3 * 4  # Máquina no 1º andar
tempo2 = a1 * 2 + a2 * 0 + a3 * 2  # Máquina no 2º andar
tempo3 = a1 * 4 + a2 * 2 + a3 * 0  # Máquina no 3º andar

# Determinação do menor tempo usando if-else
if tempo1 <= tempo2 and tempo1 <= tempo3:
    menor_tempo = tempo1
elif tempo2 <= tempo1 and tempo2 <= tempo3:
    menor_tempo = tempo2
else:
    menor_tempo = tempo3

# Saída do resultado
print(menor_tempo)