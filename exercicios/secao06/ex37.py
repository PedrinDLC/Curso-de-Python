for num in range(1000, 10000):
    n = str(num)
    a = n[0:2]
    b = n[2:]
    soma = int(a) + int(b)
    if soma**2 == num:
        print(num)
