precoLitroAlcool, precoLitroGasolina, rendimentoAcool, rendimentoGasolina = map(float, input().split())

alcool = precoLitroAlcool / rendimentoAcool
gasolina = precoLitroGasolina / rendimentoGasolina

if(alcool < gasolina):
     print("A")
else:
    print("G")
