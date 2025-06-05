import sys

try:
    # condições de valor > 0 movidas para o else:
    multiplicador = int(input('digite o multiplicador: '))
    multiplicando = int(input('digite o multiplicando: '))

except ValueError:
    sys.exit('ERRO: digite um valor numérico inteiro positivo.')

except Exception as exc:
    sys.exit(f'ERRO: {exc}.')

else:
    # condições de valor > 0 aqui
    if multiplicador <= 0:
        sys.exit('ERRO: digite um multiplicador positivo.')

    if multiplicando <= 0:
        sys.exit('ERRO: digite um multiplicando positivo.')

    '''i = 1
    resultado = 0
    while i <= multiplicador:
        i += 1
        print(f'{resultado} + {multiplicando} = {resultado + multiplicando}')
        resultado += multiplicando 
    print('FIM DA TABUADA.')

    #logica do professor
    produto = 0
    contador = 1
    while contador <= multiplicador: 
        produto += multiplicando
        contador += 1
    print(f'{multiplicador} X {multiplicando} = {produto}')
    '''
    produto = 0
    for contador in range(1, multiplicador + 1, 1):
        print(f'{produto} + {multiplicando} = {produto + multiplicando}')
        produto += multiplicando