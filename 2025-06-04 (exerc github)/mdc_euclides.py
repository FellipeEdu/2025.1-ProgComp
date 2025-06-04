import sys

try:
    numA = int(input('digite o 1° numero: '))
    numB = int(input('digite o 2° numero: '))

except ValueError:
    sys.exit('ERRO: digite um valor numérico inteiro positivo.')

except Exception as exc:
    sys.exit(f'ERRO: {exc}.')

else:     
    dividendo = numB
    # quociente = numA // numB
    resto_div = numA % numB # 270 % 210 = 60

    for cont in range(0, 100, 1):
        resto_final = dividendo % resto_div # 210 % 60 = 30
        if resto_final == 0:
            break
        else:
            dividendo = resto_div # dividendo = 60
            resto_div = resto_final # resto div = 30
        
    print(f'MDC de {numA} e {numB} é: {dividendo}')