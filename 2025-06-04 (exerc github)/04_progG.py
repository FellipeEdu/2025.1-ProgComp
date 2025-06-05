import sys

try:
	termoInicial = float(input('digite o 1° termo da PG: '))
	razao = float(input('digite a razão da PG: '))
	elementos = int(input('quantidade de elementos da PG: '))

	if razao == 0:
    		sys.exit('ERRO: razao deve ser maior que 0.')

except ValueError:
    sys.exit('ERRO: digite um valor numérico inteiro.')

except Exception as exc:
    sys.exit(f'ERRO: {exc}.')

else:
	for contador in range(1, elementos + 1, 1):
		termoGeral = termoInicial * (razao ** (contador - 1))
		print(f'{contador}° Elemento = {termoGeral}')

	if razao > 1:
		print('\nEssa PG é crescente.')
	elif razao < 1 and razao > 0:
		print('Essa PG é descrescente.')
	elif razao == 1:
		print('Essa PG é constante.')
	elif razao < 0:
		print('Essa PG é oscilante/alternada.')

	soma = (termoInicial * ((razao ** elementos) - 1)) / (razao - 1)
	print(f'Soma dos {elementos} primeiros elementos da PG = {soma}\n')

	termoDesejado = int(input('informe um elemento desejado da PG: '))

	termoGeralDesejado = termoInicial * (razao ** (termoDesejado - 1))
	print(f'{termoDesejado}° Termo = {termoGeralDesejado}')