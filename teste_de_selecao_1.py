entrada = input().split()

valor_A = int(entrada[0])
valor_B = int(entrada[1])
valor_C = int(entrada[2])
valor_D = int(entrada[3])

if valor_B > valor_C and valor_D > valor_A and valor_C + valor_D > (valor_A + valor_B) and valor_A % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores não aceitos')