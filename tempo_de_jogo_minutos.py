entrada = list(map(int, input().split()))

hora_inicial = entrada[0]
minuto_inicial = entrada[1]

hora_final = entrada[2]
minuto_final = entrada[3]

tempo_inicial = 60 * hora_inicial + minuto_inicial
tempo_final = 60 * hora_final + minuto_final
tempo = tempo_final - tempo_inicial
horas = tempo // 60
minutos = tempo % 60

if tempo > 0:
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
else:
    resultado = tempo + 1440
    print(f'O JOGO DUROU {resultado // 60} HORA(S) E {minutos % 60} MINUTO(S)')