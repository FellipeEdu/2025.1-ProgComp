import sys

try:
    num_fatores = int('digite quantos fatores primos voce quer: ')

    if num_fatores < 2:
            sys.exit('ERRO: o numero de fatores deve ser maior que 1.')

except ValueError:
    sys.exit('ERRO: digite um valor numérico inteiro positivo.')

except Exception as exc:
    sys.exit(f'ERRO: {exc}.')

else:
    print(f'Os {num_fatores} primeiros numeros com {num_fatores} fatores primos são: ')

    for contadorNumeros in range(1, num_fatores + 1, 1): # vai controlar o calc dos N primeiros numeros q podem ser decompostos em N fatores
        #numero = 2
        for numero in range(4, 1000, 1): # vai controlar o calculo de varios numeros verificando quais podem ser decompostos por N valores primos         
            divisorPrimo = 2
            contDivisorPrimo = 0
            while divisorPrimo <= numero: 
                # verificar se divisorPrimo é primo
                testePrimo = 2
                while divisorPrimo <= testePrimo:

                if (divisorPrimo % )
                if (numero % divisorPrimo) == 0:
                    divisorPrimo += 1
                    contDivisorPrimo += 1
                
