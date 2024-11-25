# Retorna o menor valor entre a e b
def f1(a, b):
    if a > b:
        return b
    else: 
        return a

# Soma o menor valor entre b e c, e em seguida soma com o 
# menor valor entre c e a para no final mostrar a soma de x + y
def f2(a,b,c):
    x = f1(b,c)
    y = x+f1(c,a)
    return x+y

print(f2(10, 20, 15))
print(f2(20, 10, 30))