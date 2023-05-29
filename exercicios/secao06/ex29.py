from math import factorial as fat
termos = 5
s = 0

for i in range(1, termos):
    s += i / fat(i*2)

print(f'S = {s}')
