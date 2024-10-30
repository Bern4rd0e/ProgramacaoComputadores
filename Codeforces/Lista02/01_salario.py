nome = input()
horasTrabalhada = float(input())
valorHoraTrabalhada = float(input())

calculo = horasTrabalhada * valorHoraTrabalhada

valorTrabalho = "{:.2f}".format(calculo)
print(nome[:20])
print("R$",valorTrabalho)

