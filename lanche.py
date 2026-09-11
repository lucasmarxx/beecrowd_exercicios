lanches = [('Cachorro-Quente', 4), ('X-Salada', 4.5), ('X-Bacon', 5), ('Torrada', 2), ('Refrigerante', 1.5)]
for i, (lanche, valor) in enumerate(lanches):
    print(f'{i+1}: {lanche}, R$ {valor:.2f}')

print('Digite o código do lanche e a quantidade desejada.')
entrada = input().split()
precos = [4, 4.5, 5, 2, 1.5]

codigo = int(entrada[0])
quantidade = int(entrada[1])
valor_a_pagar = quantidade * lanches[codigo - 1][1]

print(f'Total: R$ {valor_a_pagar:.2f}')