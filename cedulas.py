entrada = int(input())

valores_cedulas = [100, 50, 20, 10, 5, 2, 1]

valor_entrada = entrada

quantidade_cedulas = []

for cedula in valores_cedulas:
    quantidade = valor_entrada // cedula
    quantidade_cedulas.append(quantidade)
    valor_entrada = valor_entrada % cedula

print(entrada)
for quantidade in range(len(quantidade_cedulas)):
    print(f'{quantidade_cedulas[quantidade]} nota(s) de R${valores_cedulas[quantidade]},00\n')