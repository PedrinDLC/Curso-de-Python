print('Digite uma data: ')
dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))
print(f'{dia}/{mes}/{ano}')
if ano > 0:
    if 1 <= mes <= 12:
        if mes == 1:
            if 1 <= dia <= 31:
                print('Data Válida!')
            else:
                print('Dia inválido!')
        elif mes == 2:
            if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
                if 1 <= dia <= 29:
                    print('Data Válida!')
                else:
                    print('Dia inválido!')
            else:
                if 1 <= dia <= 28:
                    print('Data Válida!')
                else:
                    print('Dia inválido!')
        elif mes == 3:
            if 1 <= dia <= 31:
                print('Data Válida!')
            else:
                print('Dia inválido!')
        elif mes == 4:
            if 1 <= dia <= 30:
                print('Data Válida!')
            else:
                print('Dia inválido!')
        elif mes == 5:
            if 1 <= dia <= 31:
                print('Data Válida!')
            else:
                print('Dia inválido!')
        elif mes == 6:
            if 1 <= dia <= 30:
                print('Data Válida!')
            else:
                print('Dia inválido!')
        elif mes == 7:
            if 1 <= dia <= 31:
                print('Data Válida!')
            else:
                print('Dia inválido!')
        elif mes == 8:
            if 1 <= dia <= 31:
                print('Data Válida!')
            else:
                print('Dia inválido!')
        elif mes == 9:
            if 1 <= dia <= 30:
                print('Data Válida!')
            else:
                print('Dia inválido!')
        elif mes == 10:
            if 1 <= dia <= 31:
                print('Data Válida!')
            else:
                print('Dia inválido!')
        elif mes == 11:
            if 1 <= dia <= 30:
                print('Data Válida!')
            else:
                print('Dia inválido!')
        elif mes == 12:
            if 1 <= dia <= 31:
                print('Data Válida!')
            else:
                print('Dia inválido!')
    else:
        print('Mês inválido!')
else:
    print('Ano inválido!')
