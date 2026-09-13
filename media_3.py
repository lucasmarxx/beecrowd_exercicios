entradas = input().split()

n1 = float(entradas[0])
n2 = float(entradas[1])
n3 = float(entradas[2])
n4 = float(entradas[3])

pesos = [2, 3, 4, 1] #peso para cada nota da entrada, respectivamente
# notas = [n1, n2, n3, n4]

nota1 = n1 * pesos[0]
nota2 = n2 * pesos[1]
nota3 = n3 * pesos[2]
nota4 = n4 * pesos[3]

soma_notas = nota1 + nota2 + nota3 + nota4
soma_pesos = pesos[0]+ pesos[1]+ pesos[2]+ pesos[3]

media_final = soma_notas / soma_pesos


print(f'Média: {media_final:.1f}')
if media_final >= 7.0:
    print('Aluno aprovado.')

if media_final >= 5.0 and media_final <= 6.9:
    print('Aluno em exame.')
    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame}')
    media_com_exame = (nota_exame + media_final) / 2
    if media_com_exame > 5.0:
        print(f'Aluno aprovado.\nMédia final: {media_com_exame}')
    else:
        print('Aluno reprovado.')