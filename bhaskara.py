import math

# ERRADO
entrada = list(map(float,input().split()))
a, b, c = entrada


delta = pow(b, 2) - 4 * a * c
raiz_de_delta = math.sqrt(delta)

if a == 0 or delta < 0:
    print('Impossivel calcular')
else:
    raiz_1 = (-b + raiz_de_delta) / (2 * a)
    raiz_2 = (-b - raiz_de_delta) / (2 * a)
    print(f'R1 = {raiz_1:.5f}\nR2 = {raiz_2:.5f}')


import math


# CERTO
entrada = list(map(float,input().split()))
a, b, c = entrada

delta = pow(b, 2) - 4 * a * c

if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    raiz_de_delta = math.sqrt(delta)
    raiz_1 = (-b + raiz_de_delta) / (2 * a)
    raiz_2 = (-b - raiz_de_delta) / (2 * a)
    print(f'R1 = {raiz_1:.5f}\nR2 = {raiz_2:.5f}')