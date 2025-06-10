import sys

try:
    num = int(input('digite os N primeiros numeros desejados da sequencia de fibonacci: '))

    if num <= 0:
        sys.exit('ERRO: o numero deve ser maior que zero.')

except ValueError:
    sys.exit('ERRO: digite um valor numérico inteiro positivo.')

except Exception as exc:
    sys.exit(f'ERRO: {exc}.')

else:
    numAnterior = 0
    numAtual = 1

    for contador in range(1, num + 1, 1):
        fib = numAnterior + numAtual    # fib = 0 + 1  = 1 | 1 + 1 = 2
        numAnterior = numAtual          # ant = 1 | ant = 1 
        numAtual = fib                  # atual = 1 | atual = 2
        #print(f'{contador}°: {fib}')
        print(f'{fib}, ', end = '')

    #print(f'O {num}° numero da sequencia de fibonacci é: {fib}\n')