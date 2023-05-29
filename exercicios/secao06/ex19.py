num = 0

while num < 100 or num > 999:
    num = int(input('Digite um número inteiro entre 100 e 999: '))

num = str(num)

for c in num:
    print(c)
