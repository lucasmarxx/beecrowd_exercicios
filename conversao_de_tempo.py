entrada = int(input())

minuto = 60
hora = 600


horas = entrada // hora
minutos = entrada // minuto
segundos = entrada % minuto

print(entrada % minuto)
print(f'horas: {horas}\nminutos: {minutos}\nsegundos: {segundos}')
print(f'{horas}:{minutos}:{segundos}')