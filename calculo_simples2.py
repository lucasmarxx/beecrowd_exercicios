entrada1 = input().split()
entrada2 = input().split()

codigo1 = int(entrada1[0])
qtd1 = int(entrada1[1])
valor1 = float(entrada1[2])


codigo2 = int(entrada2[0])
qtd2 = int(entrada2[1])
valor2 = float(entrada2[2])


total_a_pagar = (qtd1 * valor1) + (qtd2 * valor2)

print(f'VALOR A PAGAR: R$ {total_a_pagar:.2f}')
