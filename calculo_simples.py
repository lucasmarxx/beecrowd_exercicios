pecas = {
    1: 5.30,
    2: 15,
    3: 22,
    4: 40
}



codigo = int(input('digite o código da peça comprada: '))
qtd_itens = int(input('digite a quantidade de itens comprados: '))


total_a_pagar = qtd_itens * pecas[codigo]

print(pecas[1])

print(f'Valor total a pagar: R${total_a_pagar:.2f}')