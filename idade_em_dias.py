dias_input = int(input(''))
valor_entrada = dias_input

dias = [365, 30, 1]
quantidades = []


for quantidade in dias:
    qtd_dias = valor_entrada // quantidade
    quantidades.append(qtd_dias)
    valor_entrada = valor_entrada % quantidade

print(f'{quantidades[0]} ano(s)\n{quantidades[1]} mes(es)\n{quantidades[2]} dia(s)')