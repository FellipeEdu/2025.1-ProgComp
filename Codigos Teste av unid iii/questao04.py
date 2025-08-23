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
    '''lstPotenciaisPrimos = [potPrimo for potPrimo in range(2, maxPrimos + 1)]'''
    
    # 1. Cria uma lista de booleanos. A posição 'i' vai representar o número 'i'.
    # Começamos com todos True (potenciais primos).
    lstNaoPrimos = [True] * (maxPrimos + 1)    
    lstNaoPrimos[0] = lstNaoPrimos[1] = False # 0 e 1 não são primos

    # 2. Percorre os números a partir do 2
    for numero in range(2, maxPrimos + 1):
        # 3. Se o número ainda é considerado primo... (ou seja, está marcado como True em lstNaoPrimos)
        if lstNaoPrimos[numero]:
            # ... marca todos os seus múltiplos como não-primos.
            # Começamos de 2*numero para não incluir o próprio número.
            multiplicador = 2
            multiplicacao = numero * multiplicador

            while multiplicacao <= maxPrimos:
                # Usa o array booleano para marcar.
                # A verificação 'if (multiplicacao not in lstNaoPrimos)' se torna desnecessária, pois simplesmente "riscamos" o número.
                lstNaoPrimos[multiplicacao] = False
                multiplicador += 1
                multiplicacao = numero * multiplicador

    # 4. Filtra a lista final de primos.
    lstPrimos = [i for i, eh_primo in enumerate(lstNaoPrimos) if eh_primo]

    '''for numero in lstPotenciaisPrimos:
        if numero not in lstNaoPrimos:
            #multiplicacao = 0
            multiplicador = 2 # inicia em 2 para não add o próprio número em lstNaoPrimos
            multiplicacao = numero * multiplicador # evita add 0 em lstNaoPrimos

            while multiplicacao <= maxPrimos:
                if (multiplicacao not in lstNaoPrimos): lstNaoPrimos.append(multiplicacao)
                multiplicacao = numero * multiplicador
                multiplicador += 1
        else: continue

    lstPrimos = [primo for primo in lstPotenciaisPrimos if primo not in lstNaoPrimos]'''
    
    print(f'Números Primos até {maxPrimos}:')
    print(lstPrimos)
    print(f'Quantidade de primos: {len(lstPrimos)}')