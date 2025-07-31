import sys, mathtools

try:
    numeroA = int(input('Digite o número A: '))
    numeroB = int(input('Digite o número B: '))

    print(f'MDC de {numeroA}, {numeroB} = {mathtools.mdc(numeroA, numeroB)}')
except ValueError:
    sys.exit('ERRO: valor inválido.')
except Exception as erro:
    sys.exit(f'ERRO: {erro}.')