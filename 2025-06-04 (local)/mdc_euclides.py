import sys

try:
    numA = int(input('digite o 1° numero: '))
    numB = int(input('digite o 2° numero: '))

    if numA < numB:
        sys.exit('ERRO: o 1° numero deve ser maior que o 2°.')

except ValueError:
    sys.exit('ERRO: digite um valor numérico inteiro positivo.')

except Exception as exc:
    sys.exit(f'ERRO: {exc}.')

else:
    dividendo = numB
    resto_divisor = numA % numB # 60

    '''
    while resto_final <= 0:
        resto_final = dividendo % resto_divisor # 210 % 60 = 30 | 60 % 30 = 0
        dividendo = resto_divisor # div = 60
        resto_divisor = resto_final # resto_div = 30
    ''' 

    if resto_divisor == 0: 
        print(f'MDC de {numA} e {numB} = {numB}.') 

    else:
        for contador in range(0, 1000, 1):
            resto_final = dividendo % resto_divisor
            if resto_final == 0:
                break
            else:
                dividendo = resto_divisor
                resto_divisor = resto_final
    
        print(f'MDC de {numA} e {numB} = {resto_divisor}.') 