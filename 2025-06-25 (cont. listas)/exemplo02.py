import sys, random

try:
    numero = int(input('Digite o valor de N (0 a 100): '))
    if not (1 <= numero <= 100):
        sys.exit('\nERRO: informe um valor positivo e até 100')

except ValueError:
    sys.exit('\nERRO: informe um valor inteiro válido.')

except Exception as excecao:
    sys.exit(f'\nERRO: {excecao}')

else:
    lstNumeros = list()
    lstQuadrados = list()

    for _ in range(numero):
        lstNumeros.append(random.randint(0, 1000))

    for quadrados in range(len(lstNumeros)):
        lstQuadrados.insert(quadrados, lstNumeros[quadrados] ** 0.5)

    print(f'{lstNumeros}\n')
    print({lstQuadrados})