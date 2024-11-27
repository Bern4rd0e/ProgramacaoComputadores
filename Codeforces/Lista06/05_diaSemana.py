def dia_da_semana(h,d):
    semana = ["Domingo", "Segunda-feira", "Terca-feira", 
         "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]


    dia = semana.index(h)

    data = (dia + d) % 7
    dt = semana[data]

    return dt

# h = "Quarta-feira"
# d = 30
# print(dia_da_semana(h, d))



