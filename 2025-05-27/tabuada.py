try:
    mult = int(input('Informe o multiplicador: '))

except ValueError:
    print('ERRO: Digite um valor inteiro.')

except Exception as exc:
    print(f'ERRO: {exc}')

else:
    res = mult * 1
    print(f'{mult} x 1 = {res}')

    res = mult * 2
    print(f'{mult} x 2 = {res}')

    res = mult * 3
    print(f'{mult} x 3 = {res}')

    res = mult * 4
    print(f'{mult} x 4 = {res}')

    res = mult * 5
    print(f'{mult} x 5 = {res}')

    res = mult * 6
    print(f'{mult} x 6 = {res}')

    res = mult * 7
    print(f'{mult} x 7 = {res}')

    res = mult * 8
    print(f'{mult} x 8 = {res}')

    res = mult * 9
    print(f'{mult} x 9 = {res}')
    
    res = mult * 10
    print(f'{mult} x 10 = {res}')