entrada = list(map(float, input().split()))

valores_positivos = 0

for numero in entrada:
    if numero > 0:
        valores_positivos += 1

print(f'{valores_positivos} valores positivos')