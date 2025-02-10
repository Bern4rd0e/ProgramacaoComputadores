N = int(input())

A = 0 
B = 0  

operacoes = list(map(int, input().split()))

for op in operacoes:
    if op == 1:
        A = 1 - A 
    elif op == 2:
        A = 1 - A 
        B = 1 - B  

print(A)
print(B)