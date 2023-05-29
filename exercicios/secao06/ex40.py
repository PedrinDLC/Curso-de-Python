n = int(input('Digite o valor de n: '))
print()

for i in range(1, n+1):
    for j in range(n - i, 0, -1):  # imprime espaços
        print(' ', end='')
    for j in range(1, i+1):   # imprime *
        print('#', end='')
    print(' ', end='')
    for j in range(1, i+1):   # imprime *
        print('#', end='')
    print()
