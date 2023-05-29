cont = 0
num = int(input("Informe um número: "))
while True:
    if num % 11 == 0 or num % 13 == 0 or num % 17 == 0:
        print(num, end='')
        if num % 11 == 0:
            print(f' é o primeiro multiplo de 11 após {num - cont}')
        elif num % 13 == 0:
            print(f' é o primeiro multiplo de 13 após {num - cont}')
        elif num % 17 == 0:
            print(f' é o primeiro multiplo de 17 após {num - cont}')
        break
    num += 1
    cont += 1
