# Como já mencionado, a leitura usando a função input() sempre produz um valor
# do tipo texto/string. É necessário usar uma função que converte a sequencia de
# símbolos/caracteres de um texto e gera o valor inteiro ou real equivalente. As funções
# int() e float() realizam as conversões para inteiro e real, respectivamente.
# Modifique o programa anterior para ler os dados, convertê-los em inteiros, realizar
# a soma, e mostrar o valor da soma. O novo programa é mostrado a seguir.

l = input()
x = int(l)
l = input()
y = int(l)
s = x+y
print(s)

# O programa agora mostra o resultado esperado para a soma entre os dois valores
# digitados.

# Saída (Será colocado como se tivessemos usado o valor 10 para l e 20 para x): 
# 10
# 20
# 30

# Observa-se que a variável l é usada 2 vezes, apenas para armazenar temporari-
# amente o valor lido quando o programa espera o usuário informar os dados. Como
# a leitura está sendo feita e o valor usado é diretamente a conversão para inteiro, é
# possível ler e converter diretamente na linha que realiza a leitura. O código a seguir
# simplifica a compreensão do programa que lê dois valores e realiza a soma.

x = int(input())
y = int(input())
s = x+y
print(s)

# O programa modificado para tratamento de números reais é mostrado a seguir:

x = float(input())
y = float(input())
s = x+y
print(s)
