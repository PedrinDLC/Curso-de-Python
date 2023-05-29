num = int(input('Digite um número: '))

for i in range(num, -1, -1):
    if i % 2 == 1:
        print(i, end=' ')
