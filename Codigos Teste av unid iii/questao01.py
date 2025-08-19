import sys, random

try:
    elementos = int(input('Digite a quantidade de elementos de cada lista: '))
    subListas = int(input('Digite a quantidade de listas: '))

except ValueError:
    sys.exit('\nERRO: informe um valor inteiro válido.')

except Exception as excecao:
    sys.exit(f'\nERRO: {excecao}')

else:
    lstPrincipal = list()
    lstTransposta = list()
    lstAux = list()

    for _ in range(subListas):
        lstSub = [random.randint(0,100) for _ in range(elementos)]
        lstPrincipal.append(lstSub)

    for sub in range(elementos): # ex: matriz 4(elementos) x 3(sublistas)
        # [1, 10, 2, 20][3, 30, 4, 40][5, 50, 6, 60] -> [1,3,5][10,30,50][2,4,6][20,40,60]
        lstAux = [lstPrincipal[elemento][sub] for elemento in range(subListas)]
        lstTransposta.append(lstAux) 

    print('\nLista Normal:')
    for sub in lstPrincipal: print(sub)
    print('\nLista Transposta:')
    for transposta in lstTransposta: print(transposta) 