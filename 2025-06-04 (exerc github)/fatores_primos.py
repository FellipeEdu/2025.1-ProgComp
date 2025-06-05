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

    for contadorNumeros in range(1, num_fatores + 1, 1): # vai ocontrolar o calc dos N primeiros numeros q podem ser decompostos em N fatores
        #numero = 2
        for numero in range(2, 1000, 1): # vai controlar o calculo de varios numeros verificando quais podem ser decompostos por N valores primos         
            divisorPrimo = 2
            while divisorPrimo <= numero: # verificar se é primo
                if (numero % divisorPrimo) == 0:
                    contDivisor += 1
                    break
                else:
                    divisores += 1
