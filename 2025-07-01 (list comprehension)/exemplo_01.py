'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);

      2) Gere uma lista com N valores inteiros aleatórios entre -100 e +100;
   
      3) A partir da lista gerada, gere uma segunda uma lista apenas com os 
         números pares da lista;
'''
import sys, random

try:
    numero = int(input('Digite o valor de N: '))
    if not (1 <= numero <= 100):
        sys.exit('\nERRO: informe um valor positivo e até 100')

except ValueError:
    sys.exit('\nERRO: informe um valor inteiro válido.')

except Exception as excecao:
    sys.exit(f'\nERRO: {excecao}')

else:
    lstNumeros = list()
    lstPares = list()

    '''
    for _ in range(numero):
        lstNumeros.append(random.randint(-100, 100))

    for pares in range(len(lstNumeros)):
        if lstNumeros[pares] % 2 == 0:
            lstPares.append(lstNumeros[pares])
    '''
    lstNumeros = [random.randint(-100, 100) for _ in range(numero)]

    lstPares = [pares for pares in lstNumeros if pares % 2 == 0]

    print(f'{lstNumeros}\n')       
    print(lstPares)