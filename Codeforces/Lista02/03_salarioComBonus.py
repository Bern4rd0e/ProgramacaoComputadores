nome = input()
salario = float(input())
numeroVendas = float(input())

comissao = "{:.2f}".format((numeroVendas * 0.15) + salario)

print(nome)
print("R$",comissao)

