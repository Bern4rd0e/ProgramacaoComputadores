def div_impar(n, div):
    if div == 1:
        return 1
    if div % 2 != 0 and n % div == 0:
        return 1 + div_impar(n, div - 1)
    else:
        return 0 + div_impar(n, div - 1)

def impar(n):
    print(div_impar(n, n))

print(impar(10))

