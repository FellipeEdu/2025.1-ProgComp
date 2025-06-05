import sys

try:
    mult = int(input('Informe o multiplicador: '))
    if mult < 0:
        sys.exit('ERRO: digite um numero positivo.')

except ValueError:
    print('ERRO: digite um valor inteiro.')

except Exception as exc:
    print(f'ERRO: {exc}')

else:

    '''
    multiplicando = 1
    while multiplicando <= 10:
        print(f'{mult} x {multiplicando} = {mult * multiplicando}')
        multiplicando += 1
    '''
    
    for multiplicando in range(1, 11, 1):
        print(f'{mult} x {multiplicando} = {mult * multiplicando}')
    
    print('FIM DA TABUADA...')