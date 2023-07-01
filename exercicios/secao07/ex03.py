num = []
quad = []

for i in range(10):
    num.append(int(input(f'Digite o {i+1}° número: ')))

print(num)

for n in range(10):
    quad.append(num[n]**2)

print(quad)
