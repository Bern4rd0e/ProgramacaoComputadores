simul = int(input())
cont = 0

for i in range(simul):
    num = int(input())   
    if num != 1:
        cont += 1

print(cont)