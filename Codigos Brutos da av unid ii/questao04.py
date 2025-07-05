import sys

try:
    numero = int(input('Digite um número: '))
    if numero <= 0:
        sys.exit('ERRO: o número deve ser positivo.')

except ValueError:
    print('ERRO: digite um valor válido.')

except Exception as excecao:
    print(f'ERRO: {excecao}')

else:
    # transforma em string pra identificar o tamanho do numero
    strNumero = str(numero)
    tamanhoNumero = 0

    for digito in strNumero:
        tamanhoNumero += 1

    numeroDividendo = numero
    soma_Potencia_Digitos = 0

    # vai somar cada digito elevado a quant de digitos
    for digitoNum in range(tamanhoNumero - 1, -1, -1):
        soma_Potencia_Digitos += (numeroDividendo // (10 ** digitoNum)) ** tamanhoNumero
        numeroDividendo %= 10 ** digitoNum

    if soma_Potencia_Digitos == numero:
        
        # formatação 370 = 3^3 + 7^3 + 0^3
        print(f'{numero} é um número de armstrong.')
        print(f'{numero} = ', end='')

        primeiroAlg = True
        for alg in strNumero:
            if not primeiroAlg: print('+', end=' ')
            
            print(f'{alg}^{tamanhoNumero}', end=' ')
            primeiroAlg = False
    
    else:
        print(f'{numero} não é um número de armstrong.')