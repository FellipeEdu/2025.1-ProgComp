import sys

numero = None

try:
    numero = int(input('Digite um numero para calcular seu fatorial: '))

except ValueError: 
    sys.exit('ERRO: Digite um número inteiro positivo')

except Exception as exc:
    sys.exit(f'ERRO: {exc}')

else:
    if numero < 0:
        print('Não existe fatorial.')
    if numero < 2:
        print(f'Fatorial de {numero} = 1')

    else:
        resultado = numero
        #contador = numero - 1
        
        '''while contador > 1:
            resultado *= contador
            contador -= 1
        
        print(f'Fatorial de {numero} = {resultado}')'''
    
        for contador in range(numero - 1, 1, -1):
            resultado *= contador
        
        print(f'Fatorial de {numero} = {resultado}')