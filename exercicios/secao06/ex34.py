n = 1

while True:
    check = 0
    for i in range(1, 11):
        check += n % i

    if check == 0:
        print(f'O menor divisível é: {n}.')
        break
    n += 1
