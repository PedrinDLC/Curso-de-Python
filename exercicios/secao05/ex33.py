preco_antigo = float(input('Informe o antigo preço do produto: '))
preco_novo = 0

if preco_antigo <= 50:
    preco_novo = preco_antigo * 1.05
elif 50 < preco_antigo <= 100:
    preco_novo = preco_antigo * 1.1
elif preco_antigo > 100:
    preco_novo = preco_antigo * 1.15

if preco_novo <= 80:
    print(f'O novo preço é de R${preco_novo:.2f}. Barato!')
elif 80 < preco_novo <= 120:
    print(f'O novo preço é de R${preco_novo:.2f}. Normal!')
elif 120 < preco_novo <= 200:
    print(f'O novo preço é de R${preco_novo:.2f}. Caro!')
elif preco_novo > 200:
    print(f'O novo preço é de R${preco_novo:.2f}. Muito caro!')
