print('Soma dos 50 primeiros números pares: ')

soma = cont = num = 0

while cont <= 50:
    if num % 2 == 0:
        soma += num
        cont += 1
    num += 1

print(f'Somatório: {soma}')
