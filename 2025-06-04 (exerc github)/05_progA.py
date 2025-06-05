import sys

try:
	termoInicial = float(input('digite o 1° termo da PA: '))
	razao = float(input('digite a razão da PA: '))
	elementos = int(input('quantidade de elementos da PA: '))

except ValueError:
    sys.exit('ERRO: digite um valor numérico inteiro.')

except Exception as exc:
    sys.exit(f'ERRO: {exc}.')

else:
	for contador in range(1, elementos + 1, 1):
		termoGeral = termoInicial + ((contador - 1) * razao)
		print(f'{contador}° Elemento = {termoGeral}')

	if razao > 0:
		print('\nEssa PA é crescente.')
	elif razao == 0:
		print('\nEssa PA é constante.')
	elif razao < 0:
		print('\nEssa PA é descrescente.')

	soma = (termoInicial * ((razao ** elementos) - 1)) / (razao - 1)
	print(f'Soma dos {elementos} primeiros elementos da PG = {soma}\n')

	termoDesejado = int(input('informe um elemento desejado da PG: '))

	termoGeralDesejado = termoInicial * (razao ** (termoDesejado - 1))
	print(f'{termoDesejado}° Termo = {termoGeralDesejado}')