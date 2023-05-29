print('-='*10)
print('Cálculo de média')
print('-='*10)
print('Informe 3 números: ')
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

print('Selecione uma das opções de média: ')
print('(a) Geométrica.')
print('(b) Ponderada.')
print('(c) Harmônica')
print('(d) Aritimética')
op = str(input('Opção: ')).strip().lower()[0]

if op == 'a':
    media = (x * y * z) ** (1/3)
    print(f'Média Geométrica: {media:.2f}')
elif op == 'b':
    media = (1*x + 2*y + 3*z) / 6
    print(f'Média Ponderada: {media}')
elif op == 'c':
    media = 1 / (1/x + 1/y + 1/z)
    print(f'Média Harmônica: {media}')
elif op == 'd':
    media = (x + y + z) / 3
    print(f'Média Aritimética: {media}')
else:
    print('Opção inválida!')
