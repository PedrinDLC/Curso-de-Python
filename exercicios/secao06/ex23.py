num = int(input("Digite um número: "))
print("Seus divisores são: ", end='')
for n in range(1, num+1):
    if num % n == 0:
        print(f'{n} ', end='')
