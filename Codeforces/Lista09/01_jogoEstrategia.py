jogadores, rodadas = map(int, input().split())  
pontos = list(map(int, input().split()))

pontuacoes = [0] * jogadores

for i in range(jogadores * rodadas):
    jogador = i % jogadores 
    pontuacoes[jogador] += pontos[i]

max_pontos = max(pontuacoes)
vencedor = -1

for i in range(jogadores - 1, -1, -1): 
    if pontuacoes[i] == max_pontos:
        vencedor = i + 1 
        break

print(vencedor)

