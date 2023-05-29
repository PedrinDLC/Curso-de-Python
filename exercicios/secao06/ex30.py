"""
Faça um programa que calcule as seguintes sequências:
1 + 2 + 3 + 4 + 5 + ... + n
1 - 2 + 3 - 4 + 5 + ... + n(-1)**n-1
1 + 3 + 5 + 7 + ... + (2n - 1)
"""
num = int(input('Digite um número: '))
s1 = s2 = s3 = 0
for i in range(1, num+1):
    s1 += i
    s2 += (-1) ** (i-1) * i
    s3 += 2*i - 1

print(f'Soma da primeira sequencia: {s1}')
print(f'Soma da segunda sequencia: {s2}')
print(f'Soma da terceira sequencia: {s3}')
