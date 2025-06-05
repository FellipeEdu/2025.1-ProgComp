import sys

try:
	termoInicial = int(input('digite o 1° termo da PG: '))
	razao = int(input('digite a razão da PG: '))
	elementos = int(input('quantidade de elementos da PG: '))

	if razao == 0:
    		sys.exit('ERRO: razao deve ser maior que 0.')

except ValueError:
    sys.exit('ERRO: digite um valor numérico inteiro.')

except Exception as exc:
    sys.exit(f'ERRO: {exc}.')

else:
      for elementos in range():