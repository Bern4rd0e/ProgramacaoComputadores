import math


cabine = int(input())
alunos = int(input())

supervisor = math.ceil(alunos / (cabine - 1))

print(supervisor)