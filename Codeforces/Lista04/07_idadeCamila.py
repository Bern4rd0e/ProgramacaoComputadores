idade1 = int(input())
idade2 = int(input())
idade3 = int(input())

if (idade1 > idade2 and idade1 < idade3) or (idade1 > idade3 and idade1 < idade2):
    print(idade1)
elif (idade2 > idade1 and idade2 < idade3) or (idade2 > idade3 and idade2 < idade1):
    print(idade2)
elif(idade1 == idade2) or (idade1 == idade3):
    print(idade1)
elif(idade2 == idade3):
    print(idade2)
else:
    print(idade3)
