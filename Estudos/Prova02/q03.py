def digit_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + digit_sum(n // 10)
    
res = int(input())
print(digit_sum(res))
