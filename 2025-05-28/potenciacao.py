import sys

try:
    base = int(input('digite a base: '))
    potencia = int(input('digite a potencia: '))

except ValueError:
    sys.exit('ERRO: digite um valor numérico inteiro positivo.')

except Exception as exc:
    sys.exit(f'ERRO: {exc}.')

else:
    # condições de valor > 0 aqui
    if potencia <= 0:
        sys.exit('ERRO: digite uma base positiva.')

    if potencia <= 0:
        sys.exit('ERRO: digite uma potencia positiva.')

    potenciacao = 0
    contador = 1
    while contador <= potencia:
        potenciacao *= base
        contador += 1

# OLHAR O RESTO DO CODIGO NO GITHUB DO PROF