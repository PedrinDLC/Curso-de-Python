km = float(input('Informe a distância percorrida (em Km): '))
gl = float(input('Informe a quantos litros de gasolina foram consumidos: '))
consumo = km / gl

if consumo < 8:
    print('Venda o carro!')
elif 8 <= consumo <= 14:
    print('Econômico')
else:
    print('Super econômico')
