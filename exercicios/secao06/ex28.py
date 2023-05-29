

e = 1
fat = 1
num = int(input("Digite um valor inteiro e positivo: "))

for i in range(1, num+1):
    fat = fat * i
    e += 1 / fat

print(f'E = {e}')
