media = cont = 0

while True:
    idade = int(input('Informe a idade de um indivíduo (0 para encerrar): '))
    if idade == 0:
        break
    else:
        media += idade
        cont += 1
print(f'A média de idade do grupo é de: {media / cont} anos')
