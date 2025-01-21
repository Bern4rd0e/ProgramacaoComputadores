while True:
    H1, M1, H2, M2 = map(int, input().split())
    
    if H1 == 0 and M1 == 0 and H2 == 0 and M2 == 0:
        break
    
    tempo_atual = H1 * 60 + M1
    tempo_alarme = H2 * 60 + M2
    
    if tempo_alarme > tempo_atual:
        minutos_de_sono = tempo_alarme - tempo_atual
    else:
        minutos_de_sono = (tempo_alarme + 1440) - tempo_atual
    
    print(minutos_de_sono)