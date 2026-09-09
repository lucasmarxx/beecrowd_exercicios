entrada = float(input(''))

intervalos = [[0, 25], [25, 50], [50, 75], [75, 100]]

if entrada < 0 or entrada > 100:
    print('valor incompatível!')
else:
    if entrada >= intervalos[0][0] and entrada <= intervalos[0][1]:
        print(f'Intervalo {intervalos[0]}')
    elif entrada >= intervalos[1][0] and entrada <= intervalos[1][1]:
        print(f'Intervalo {intervalos[1]}')
    elif entrada >= intervalos[2][0] and entrada <= intervalos[2][1]:
        print(f'Intervalo {intervalos[2]}')
    else:
        print(f'Intervalo {intervalos[3]}')