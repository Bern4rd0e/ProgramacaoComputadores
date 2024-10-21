# SEPARADOR

nome = input()
print("Oi", nome, ", bom dia!")

# Saída: Oi, (nome digitado), bom dia!

nome = input()
print("Oi",nome,", bom dia!", sep="A")

# Saída: OiAJorgiano ,Abom dia! 

# O separador pode ser qualquer texto, inclusive com várias letras, 
# como o exemplo mostrado anteriormente.

# Por padrão, o comando print() adiciona uma quebra de linha ao mostrar todos os
# valores listados como parâmetros. Considere o programa oi.py escrito da seguinte
# forma:

nome = input()
print("Oi")
print(nome)
print(", bom dia!")

# Saída: 
# Oi
# Jorgiano
# , bom dia!

# A separação de vários dados a serem impressos em uma mesma linha pode facilitar
# a compreensão do código escrito, onde a linha a ser impressa contém muitos dados e
# textos entre os dados. É uma prática comum em programação separar a impressão
# de uma linha em vários comandos print(). Da mesma forma que se modifica o
# separador de dados, há também como modificar o que será exibido ao fim de cada
# print(), em substituição à quebra de linha. Para tanto, usa-se a opção end=X do
# comando print(), como mostrado do código a seguir.

nome = input() # O usuário digita um nome
print("Oi",end=" ") # Imprime "Oi" e adiciona um espaço, não pula linha
print(nome,end="") # Imprime o nome sem adicionar nada no final
print(", bom dia!") # Imprime ", bom dia!" e pula para a próxima linha

