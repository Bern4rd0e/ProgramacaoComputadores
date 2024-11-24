# Entrada: número de refeições disponíveis
Ca, Ba, Pa = map(int, input().split())
# Entrada: número de refeições requisitadas
Cr, Br, Pr = map(int, input().split())

# Inicializa o total de não atendidos como zero
if Cr > Ca:
    if Br > Ba:
        if Pr > Pa:
            print((Cr - Ca) + (Br - Ba) + (Pr - Pa))
        else:
            print((Cr - Ca) + (Br - Ba))
    elif Pr > Pa:
        print((Cr - Ca) + (Pr - Pa))
    else:
        print(Cr - Ca)
elif Br > Ba:
    if Pr > Pa:
        print((Br - Ba) + (Pr - Pa))
    else:
        print(Br - Ba)
elif Pr > Pa:
    print(Pr - Pa)
else:
    print(0)