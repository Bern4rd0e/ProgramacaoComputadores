# Retorna tamanho do terreno
def terreno(l, p):
    return l * p

# def maior(a, b):
#     if a > b
#     maior = a 
#     else:
#     maior = b

largura1, profundidade1 = map(int, input().split())
largura2, profundidade2 = map(int, input().split())
largura3, profundidade3 = map(int, input().split())
largura4, profundidade4 = map(int, input().split())

print(terreno(largura1, profundidade1))
print(terreno(largura2, profundidade2))
print(terreno(largura3, profundidade3))
print(terreno(largura4, profundidade4))


