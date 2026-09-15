entrada = list(map(int,input().split()))
a, b, c = entrada

calculo = (a + b + abs(a - b)) // 2
calculo_2 = (calculo + c + abs(calculo - c)) // 2

print(f'{calculo_2} eh o maior')