entrada = int(input())
letra = input().split()
    
soma = 0
    
for i in range(len(letra)):
    if letra[i] == letra[i - 1]:  
        soma += 1
    
print(soma)
