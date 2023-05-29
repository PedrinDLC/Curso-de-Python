n = int(input('Digite um número: '))

cont = 0
num = 0

print(f'Os primeiros {n} números naturais ímpares: ')
while cont < n:
    if num % 2 == 1:
        print(num, end=' ')
        cont += 1
    num += 1
