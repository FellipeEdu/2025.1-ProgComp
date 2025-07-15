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
    lstNumeros = random.sample(range(1001), numero) #random.randint(0, 1000)
    lstQuadrados = list()

    # for _ in range(numero):
    #    lstNumeros.append(random.randint(0, 1000))

    for numeros in lstNumeros:
        lstQuadrados.append(numeros ** 0.5)

    print(f'{lstNumeros}\n')
    print(lstQuadrados)