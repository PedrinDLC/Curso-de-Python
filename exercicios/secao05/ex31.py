altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

print('Sua classificação é ', end='')

if altura < 1.2:
    if peso <= 60:
        print('A')
    elif 60 < peso <= 90:
        print('D')
    else:
        print('G')
elif 1.2 <= altura <= 1.7:
    if peso <= 60:
        print('B')
    elif 60 < peso <= 90:
        print('E')
    else:
        print('H')
else:
    if peso <= 60:
        print('C')
    elif 60 < peso <= 90:
        print('F')
    else:
        print('I')
