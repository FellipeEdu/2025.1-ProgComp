numero = int(1) # inicializa os numeros

while numero < 1000000:
    # verificar se as potencias de 5 de cada digito = numero
    soma_Potencia_Alg = 0
    numero_Dividendo = numero

    for potencia in range(5, -1, -1):
        # ex: 2678 // 10 ^ 5 = 0 ... 2678 // 10 ^ 3 = 2 --> 2 ^ 5 = 32 | 678 // 10 ^ 2 = 6 --> 6 ^ 5 = ...
        soma_Potencia_Alg += (numero_Dividendo // (10 ** potencia)) ** 5 # faz divisão por 100000 > 10000 > 1000... p/ pegar cada algarismo
        numero_Dividendo %= (10 ** potencia)
      
    if numero == soma_Potencia_Alg and ((numero % 2 == 0) or (numero % 5 == 0)):
        print(f'{numero} = ', end='')

        # formataçao para exibir: 4150 = 4^5 + 1^5 + 5^5 + 0^5
        strNumero = str(numero)

        primeiroAlg = True
        for alg in strNumero:
            if not primeiroAlg: print('+', end=' ')
            
            print(f'{alg}^5', end=' ')
            primeiroAlg = False
        print()

    numero += 1