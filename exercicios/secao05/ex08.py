n1 = float(input('Informe a primeira nota: '))
if n1 > 10:
    print('Nota inválida!')
elif n1 < 0:
    print('Nota inválida!')
else:
    n2 = float(input('Informe a segunda nota: '))
    if n2 > 10:
        print('Nota inválida')
    elif n2 < 0:
        print('Nota inválida!')
    else:
        media = (n1 + n2) / 2
        print(f'A média destas notas é de {media:.2f}')
