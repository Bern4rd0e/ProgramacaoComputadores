precoLitroAlcool, precoLitroGasolina, rendimentoAcool, rendimentoGasolina = map(float, input().split())

if(precoLitroAlcool < precoLitroGasolina) and (rendimentoAcool > rendimentoGasolina):
    print("A")

else:
    if(rendimentoGasolina > rendimentoAcool):
        print("G")
