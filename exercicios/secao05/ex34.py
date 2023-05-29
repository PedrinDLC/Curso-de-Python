nota = float(input('Digite a nota do aluno: '))
faltas = int(input('Informe o total de faltas do aluno: '))

if 9 <= nota <= 10:
    if faltas <= 20:
        print('Conceito A')
    else:
        print('Conceito B')
elif 7.5 <= nota <= 8.9:
    if faltas <= 20:
        print('Conceito B')
    else:
        print('Conceito C')
elif 5 <= nota <= 7.4:
    if faltas <= 20:
        print('Conceito C')
    else:
        print('Conceito D')
elif 4 <= nota <= 4.9:
    if faltas <= 20:
        print('Conceito D')
    else:
        print('Conceito E')
elif 0 <= nota <= 3.9:
    if faltas <= 20:
        print('Conceito E')
    else:
        print('Conceito F')
else:
    print('Nota inválida!')
