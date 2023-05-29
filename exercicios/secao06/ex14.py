num = int(input('Digite um número: '))

for i in range(num, -1, -1):
    if i % 2 == 0:
        print(i, end=' ')
