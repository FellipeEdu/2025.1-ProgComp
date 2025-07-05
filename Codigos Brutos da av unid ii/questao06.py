import sys

try:
    numero = int(input('Digite um número: '))

    if numero <= 0 or numero > 9999:
        sys.exit('ERRO: o número deve ser positivo e com no máximo 4 digitos.')

    if numero % 1111 == 0:
        sys.exit('ERRO: o número com 4 digitos não pode ter todos os digitos iguais')

except ValueError:
    print('ERRO: digite um valor válido.')

except Exception as excecao:
    print(f'ERRO: {excecao}')

else:
    # tranforma qualquer numero em 4 digitos
    if numero < 10:
        numero *= 1000

    elif numero < 100:
        numero *= 100

    elif numero < 1000:
        numero *= 10

    strNumero = str(numero)
    strNumeroDecres = ''
    kaprekar = 0
    iteracoes = 0
    kaprekarFalho = False

    print('Iterações:')

    while kaprekar != 6174 and not kaprekarFalho:
        # ordenando strNumero decrescente
        # ex: 1500
        while strNumero:
            # encontrando o maior caractere
            maior = strNumero[0] # maior = str[0] = 1
            for num in strNumero: # 1; 5; 0; 0;
                if num > maior: # 1 > 1; 5 > 1; 0 > 1; 0 > 1
                    maior = num # 5
            # removendo a primeira ocorrência de 'maior'
            nova = ""
            removido = False
            for num in strNumero: # 1; 5; 0; 0;
                if num == maior and not removido: # 1 = 5; 5 = 5; 0 = 5; 0 = 5
                    removido = True
                    continue
                nova += num # 1; 0; 0;
            strNumeroDecres += maior # 5
            strNumero = nova # 100
        
        strNumeroCresc = int(strNumeroDecres[::-1])
        kaprekar = int(strNumeroDecres) - strNumeroCresc

        print(f'{int(strNumeroDecres):04d} - {strNumeroCresc:04d} = {kaprekar}')

        iteracoes += 1
        # zerando as variaveis de string para novas iterações
        strNumeroDecres = ''
        strNumeroCresc = ''
        strNumero = str(kaprekar)

        # confere caso o numero nao resultou numa constante de kaprekar e o calculo deu errado
        if kaprekar == 0:
            kaprekarFalho = True
            print('Não foi possível calcular a constante de Kaprekar com este valor.')

    print(f'N° de iterações: {iteracoes}')