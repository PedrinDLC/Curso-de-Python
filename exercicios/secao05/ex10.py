alt = float(input('Informe sua altura: '))
sex = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
if sex == 'M':
    print(f'Seu peso ideal serai de {(72.7 * alt) - 58:.2f}Kg')
elif sex == 'F':
    print(f'Seu peso ideal serai de {(62.1 * alt) - 44.7:.2f}Kg')
else:
    print('Sexo inválido!')
