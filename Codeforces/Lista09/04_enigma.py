def contar_posicoes_validas(mensagem_cifrada, crib):
    n = len(mensagem_cifrada)
    m = len(crib)
    
    contagem = 0
    
    for i in range(n - m + 1):
        valido = True
        for j in range(m):
            if mensagem_cifrada[i + j] == crib[j]:
                valido = False
                break
        if valido:
            contagem += 1
    
    return contagem

mensagem_cifrada = input().strip()
crib = input().strip()

resultado = contar_posicoes_validas(mensagem_cifrada, crib)
print(resultado)
