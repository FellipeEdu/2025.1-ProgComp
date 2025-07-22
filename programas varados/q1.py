import sys, random

try:
    elementos = int(input('Digite o valor dos elementos: '))
    subl = int(input('Sublistas: '))

except ValueError:
    sys.exit('\nERRO: informe um valor inteiro válido.')

except Exception as excecao:
    sys.exit(f'\nERRO: {excecao}')

else:
    lstPrincipal = list()
    for _ in range(subl):
        lstSub = list()
        for _ in range(elementos):
            lstSub.append(random.randint(0,100))
        #lstSub = [random.randint(0,100) for _ in range(elementos)]
        lstPrincipal.append(lstSub)

    print(lstPrincipal)