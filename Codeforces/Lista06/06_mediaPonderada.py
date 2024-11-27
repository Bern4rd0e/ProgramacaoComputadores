def media_ponderada(v1, p1, v2, p2):

    mediaPonderada = ((v1 * p1) + (v2 * p2)) / (p1 + p2)  

    mediaPonderada_formatada = "{:.6f}".format(mediaPonderada)

    return float(mediaPonderada_formatada)

print(media_ponderada(54,9,65,10))