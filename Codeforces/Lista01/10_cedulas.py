valor = int(input())

resto1 = valor % 100
resto2 = resto1 % 50
resto3 = resto2 % 20
resto4 = resto3 % 10
resto5 = resto4 % 5
resto6 = resto5 % 2

divisao1 = valor // 100
divisao2 = resto1 // 50
divisao3 = resto2 // 20
divisao4 = resto3 // 10
divisao5 = resto4 // 5
divisao6 = resto5 // 2
divisao7 = resto6 // 1

print(valor)
print(divisao1,"nota(s) de R$ 100,00")
print(divisao2,"nota(s) de R$ 50,00")
print(divisao3,"nota(s) de R$ 20,00")
print(divisao4,"nota(s) de R$ 10,00")
print(divisao5,"nota(s) de R$ 5,00")
print(divisao6,"nota(s) de R$ 2,00")
print(divisao7,"nota(s) de R$ 1,00")

