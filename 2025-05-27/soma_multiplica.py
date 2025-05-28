import sys

try:
    multiplicador = int(input('digite o multiplicador: '))
    if multiplicador < 0:
        sys.exit('ERRO: digite um numero positivo.')

    multiplicando = int(input('digite o multiplicando: '))
    if multiplicando < 0:
        sys.exit('ERRO: digite um numero positivo.')

except ValueError:
    sys.exit('ERRO: digite um valor numérico.')

except Exception as exc:
    sys.exit(f'ERRO: {exc}.')

else:
    i = 1
    resultado = 0
    while i <= multiplicador:
        i += 1
        print(f'{resultado} + {multiplicando} = {resultado + multiplicando}')
        resultado += multiplicando 
    print('FIM DA TABUADA.')