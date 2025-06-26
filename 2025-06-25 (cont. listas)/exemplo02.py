import sys, random

try:
    numero = int(input('Digite o valor de N: '))
    if not (1 <= numero <= 100):
        sys.exit('\nERRO: informe um valor positivo e até 100')

except ValueError:
    sys.exit('\nERRO: informe um valor inteiro válido.')

except Exception as excecao:
    sys.exit(f'\nERRO: {excecao}')

else: