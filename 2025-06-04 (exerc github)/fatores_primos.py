import sys

try:
    fatores = int('digite quantos fatores primos voce quer: ')

    if fatores <= 0:
            sys.exit('ERRO: o numero deve ser maior que zero.')

except ValueError:
    sys.exit('ERRO: digite um valor numérico inteiro positivo.')

except Exception as exc:
    sys.exit(f'ERRO: {exc}.')

else:
     print(f'Os {fatores} numeros com {fatores} fatores primos são: ')
     