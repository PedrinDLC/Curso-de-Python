maior = menor = check = 0

while True:
    num = int(input('Digite um número (< 0 para encerrar): '))
    if num < 0:
        break
    else:
        if check == 0:
            maior = menor = num
            check = 1
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
print(f'O maior numero digitado foi {maior} e o menor foi {menor}')
