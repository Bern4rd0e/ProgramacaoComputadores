valorItem = int(input())
quantidade = int(input())
valorPago = int(input())

valorTotal = valorItem * quantidade
troco = valorPago - valorTotal

print("A pagar:", valorTotal)
print("Troco  :", troco)