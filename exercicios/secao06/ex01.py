cont = 0
num = 1

print('Os 5 primeiros múltiplos de 3 são: ')

while cont < 5:
    if num % 3 == 0:
        cont += 1
        print(f'{num} ', end='')
    num += 1
