entrada = float(input())

salario = 0

if entrada > 0 and entrada < 400.00:
    salario = entrada + (entrada * 0.15)
    print(f'Novo salário: R${salario:.2f}')
    print(f'Reajuste ganho: {entrada * 0.15}')
    print('Em percentual: 15%')
elif entrada >= 400.01 and entrada <= 800.00:
    salario = entrada + (entrada * 0.12)
    print(f'Novo salário: R${salario:.2f}')
    print(f'Reajuste ganho: {entrada * 0.12}')
    print('Em percentual: 12%')
elif entrada >= 800.01 and entrada <= 1200.00:
    salario = entrada + (entrada * 0.10)
    print(f'Novo salário: R${salario:.2f}')
    print(f'Reajuste ganho: {entrada * 0.10}')
    print('Em percentual: 10%')
elif entrada >= 1200.01 and entrada <= 2000.00:
    salario = entrada + (entrada * 0.07)
    print(f'Novo salário: R${salario:.2f}')
    print(f'Reajuste ganho: {entrada * 0.07}')
    print('Em percentual: 7%')
else:
    salario = entrada + (entrada * 0.04)
    print(f'Novo salário: R${salario:.2f}')
    print(f'Reajuste ganho: {entrada * 0.04}')
    print('Em percentual: 4%')