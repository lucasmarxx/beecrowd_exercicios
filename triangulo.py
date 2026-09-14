entrada = list(map(float,input().split()))
a, b, c = entrada

if a < (b + c) and b < (a + c) and c < (a + b):
    print(f'perímetro: {a + b + c:.1f}')
else:
    print(f'área: {(a + b) * c / 2}')