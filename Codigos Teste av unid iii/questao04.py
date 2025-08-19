import sys

try:
    maxPrimos = int(input('Digite um valor entre 2 e 10**6: '))

    while not (2 <= maxPrimos <= 1000000):
        print('ERRO: digite um valor positivo entre 2 e 10**6.\n')
        maxPrimos = int(input('Digite um valor entre 2 e 10**6: '))

except ValueError:
    sys.exit('\nERRO: informe um valor inteiro válido.')

except Exception as excecao:
    sys.exit(f'\nERRO: {excecao}')
else:
    lstPotenciaisPrimos = [potPrimo for potPrimo in range(2, maxPrimos + 1)]
    lstNaoPrimos = list()

    for numero in lstPotenciaisPrimos:
        if numero not in lstNaoPrimos:
            multiplicacao = 0
            multiplicador = 2 # inicia em 2 para não add o próprio número em lstNaoPrimos
            multiplicacao = numero * multiplicador # evita add 0 em lstNaoPrimos

            while multiplicacao <= maxPrimos:
                if (multiplicacao not in lstNaoPrimos): lstNaoPrimos.append(multiplicacao)
                multiplicacao = numero * multiplicador
                multiplicador += 1
        else: continue

    lstPrimos = [primo for primo in lstPotenciaisPrimos if primo not in lstNaoPrimos]
    
    print(f'Números Primos até {maxPrimos}:')
    print(lstPrimos)