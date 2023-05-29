n = int(input('Digite um numero: '))
i = int(input('Digite o valor de i: '))
j = int(input('Digite o valor de j: '))

cont = 0
num = 0
while cont < n:
    if num % i == 0:
        print(f'{num} ', end='')
        cont += 1
    elif num % j == 0:
        print(f'{num} ', end='')
        cont += 1
    num += 1
