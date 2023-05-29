from random import randint

n = int(input('Infome o numero de lançamentos: '))

for i in range(1, n+1):
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    print(f'{i}º lançamento: ', end='')
    if d1 == d2:
        print(f'Os dois dados são iguais: {d1} e {d2}')
    elif d1 > d2:
        print(f'O dado d1 é maior que o dado d2: {d1} e {d2}')
    else:
        print(f'O dado d2 é maior que o dado d1: {d1} e {d2}')
