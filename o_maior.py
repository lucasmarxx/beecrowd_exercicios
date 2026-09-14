entrada = list(map(int,input().split()))
a, b, c = entrada
#fazer depois

calculo = (a + b + abs(a - b)) // 2
calculo_2 = (calculo + c + abs(calculo - c)) // 2

print(calculo_2)