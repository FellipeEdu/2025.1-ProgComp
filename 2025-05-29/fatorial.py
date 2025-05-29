import sys

numero = None

try:
    numero = int(input('Digite um numero para calcular seu fatorial: '))

except ValueError: 
    sys.exit('ERRO: Digite um número inteiro positivo')

except Exception as exc:
    sys.exit(f'ERRO: {exc}')

else:
    