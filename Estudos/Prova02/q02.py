lista = list(map(int,input().split()))

if len(lista) == 1:
    print(lista)
if len(lista) == 0:
    print("Não é possível mostrar")
else:
    #Quanto menor diminiur no lista[len(lista) - 1], 
    #menos uma casa é, exemplo: -1 equivale ao ultimo elemento.
    media = (lista[1] + lista[len(lista) - 1]) / 2
    print(media)