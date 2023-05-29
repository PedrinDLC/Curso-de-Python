n1 = float(input('Informe a nota do trabalho de laboratório: '))
n2 = float(input('Informe a nota da avaliação semestral: '))
n3 = float(input('Informe a nota do exame final: '))
media = (n1 * 2 + n2 * 3 + n3 * 5) / (2 + 3 + 5)
print(f'A média foi de {media:.1f}')
if media < 2.9:
    print('Reprovado!')
elif media < 4.9:
    print('Recuperação!')
else:
    print('Aprovado!')
