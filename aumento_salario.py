entrada = float(input())

salario = 0
def print_dos_salarios(percentual, entrada):
    print(f'Novo salário: {salario:.2f}')
    print(f'Reajuste ganho: {entrada * (percentual * 0.01)}')
    print(f'Em percentual: {percentual}%')


if entrada > 0 and entrada < 400.00:
    salario = entrada + (entrada * 0.15)
    print_dos_salarios(15, entrada)
elif entrada >= 400.01 and entrada <= 800.00:
    salario = entrada + (entrada * 0.12)
    print_dos_salarios(12, entrada)
elif entrada >= 800.01 and entrada <= 1200.00:
    salario = entrada + (entrada * 0.10)
    print_dos_salarios(10, entrada)
elif entrada >= 1200.01 and entrada <= 2000.00:
    salario = entrada + (entrada * 0.07)
    print_dos_salarios(7, entrada)
else:
    salario = entrada + (entrada * 0.04)
    print_dos_salarios(4, entrada)