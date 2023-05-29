num = int(input('Digite um número inteiro: '))

if num % 3 == 0 and num % 5 == 0:
    print(f'O numero {num} é divisivel por 3 e por 5')
elif num % 3 == 0:
    print(f'O número {num} é divisivel por apenas por 3')
elif num % 5 == 0:
    print(f'O número {num} é divisivel por apenas por 5')
else:
    print(f'O número {num} não é divisível por 3 ou por 5')
