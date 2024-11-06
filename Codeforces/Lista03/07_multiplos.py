n1 = int(input())
n2 = int(input())

if(n1 > n2):
    if(n1 % n2 == 0):
        print("Multiplos")
    else:
        print("Nao multiplos")
else: 
    if(n2 % n1 == 0):
        print("Multiplos")
    else:
        print("Nao multiplos")