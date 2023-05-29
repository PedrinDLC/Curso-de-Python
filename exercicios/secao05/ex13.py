n1 = float(input('Informe a nota da primeira prova: '))
n2 = float(input('Informe a nota da segunda prova: '))
n3 = float(input('Informe a nota da terceira prova: '))
mediap = (n1 * 1 + n2 * 1 + n3 * 2) / (1 + 1 + 2)
print(f'A média do aluno foi de {mediap:.2f}')
if mediap > 60:
    print('Aprovado!')
else:
    print('Reprovado!')
