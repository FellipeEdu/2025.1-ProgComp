import sys, random

try:
    elementos = int(input('Digite o valor dos elementos: '))
    subl = int(input('Sublistas: '))
    if not (1 <= elementos <= 100):
        sys.exit('\nERRO: informe um valor positivo e até 100')

except ValueError:
    sys.exit('\nERRO: informe um valor inteiro válido.')

except Exception as excecao:
    sys.exit(f'\nERRO: {excecao}')

else:
    lstPrincipal = list()
    for _ in range(subl):
        lstSub = [random.randint(0,100) for _ in range(elementos)]
        lstPrincipal.append(lstSub)

    print(lstPrincipal)