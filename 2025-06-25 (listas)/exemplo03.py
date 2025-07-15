import sys, random

try:
    numero = int(input('Digite o valor de N (0 a 100): '))

except ValueError:
    sys.exit('\nERRO: informe um valor inteiro válido.')

except Exception as excecao:
    sys.exit(f'\nERRO: {excecao}')

else:
    if not (1 <= numero <= 100):
        sys.exit('\nERRO: informe um valor positivo e até 100')

    lstNumeros = list()
    lstTrios = list()

    for _ in range(numero):
        valor = random.randint(-100, 100)

        lstNumeros.append(valor)

        lstTrios.append([valor -1, valor, valor + 1])

    print(lstNumeros)

    print(lstTrios)