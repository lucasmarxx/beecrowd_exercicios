entrada = input().split()

lanches = ['Cachorro-Quente', 'X-Salada', 'X-Bacon', 'Torrada', 'Refrigerante']
precos = [4, 4.5, 5, 2, 1.5]

codigo = int(entrada[0])
valor_a_pagar = int(entrada[1]) * precos[int(entrada[1])]

print(f'Total: R$ {valor_a_pagar:.2f}')