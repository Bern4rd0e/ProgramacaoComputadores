medicoesEqui = int(input())

soma = 0
medicoes = []

for i in range(medicoesEqui):
    medicoesCard = int(input())
    medicoes.append(medicoesCard)

    soma += medicoesCard
    mediaCard = soma // medicoesEqui

medicaoAcimaAbaixo = 0
for medicoesCard in medicoes:
    if (medicoesCard > mediaCard * 1.1 
        or medicoesCard < mediaCard * 0.9 // 1):
        medicaoAcimaAbaixo += 1

print(mediaCard)
print(medicaoAcimaAbaixo)
