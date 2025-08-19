import sys, random, os; from math import factorial

diretorio = os.path.dirname(__file__)

try:
    escritaElem = open(f'{diretorio}\\NUMEROS_ESCOLHIDOS.txt', 'w', encoding='utf-8')
    escritaComb = open(f'{diretorio}\\COMBINACOES.csv', 'w', encoding='utf-8')
    elementos = int(input('Digite o valor de N elementos: '))

    while not (7 <= elementos <= 60):
        print('ERRO: digite um valor positivo entre 7 e 60.\n')
        elementos = int(input('Digite o valor de N elementos: '))

except ValueError:
    sys.exit('\nERRO: informe um valor inteiro válido.')
except FileNotFoundError:
    sys.exit('\nERRO: arquivo não encontrado.')
except Exception as excecao:
    sys.exit(f'\nERRO: {excecao}')
else:
    lstNumeros = list()
    lstCombinacoes = list()

    for _ in range(elementos):
        numTemp = random.randint(1,60)
        # evitar repetição
        if numTemp not in lstNumeros: lstNumeros.append(numTemp)
        # adiciona um valor qualquer (nesse caso soma 1 ao valor atual) pra evitar que a lista fique com menos elementos do que o informado
        else: lstNumeros.append(numTemp + 1)

    linha = ' '.join(str(i) for i in lstNumeros)
    escritaElem.write(linha)
    escritaElem.close() 
    print("\nArquivo 'NUMEROS_ESCOLHIDOS.txt' criado com sucesso.")
    
    #combinacoes
    for num in range(len(lstNumeros)):
        for num2 in range(num + 1, len(lstNumeros)):
            for num3 in range(num2 + 1, len(lstNumeros)):
                for num4 in range(num3 + 1, len(lstNumeros)):
                    for num5 in range(num4 + 1, len(lstNumeros)):
                        for num6 in range(num5 + 1, len(lstNumeros)):
                            combinacao = [lstNumeros[num], lstNumeros[num2], lstNumeros[num3], 
                                        lstNumeros[num4], lstNumeros[num5], lstNumeros[num6]]
                            lstCombinacoes.append(combinacao)
                            lstCombinacoes[-1].sort()
    
    for comb in lstCombinacoes:
        linha = ';'.join(str(i) for i in comb)
        escritaComb.write(f'{linha}\n')
    escritaComb.close()
    print("\nArquivo 'COMBINACOES.csv' criado com sucesso.")

    combQuina = int((factorial(6) / factorial(5)) * (factorial(len(lstNumeros) - 6) / factorial((len(lstNumeros) - 6) - 1)))
    # ATENÇÃO: é impossível fazer uma QUADRA com 7 números
    if elementos > 7: combQuadra = int((factorial(6) / (factorial(4) * 2)) * (factorial(len(lstNumeros) - 6) / (2 * factorial((len(lstNumeros) - 6) - 2))))
    else: combQuadra = 0
    

    print(f'\nQuantidade de Combinações')
    print(f'SENA: {len(lstCombinacoes)}')
    print(f'QUINA: {combQuina}')
    print(f'QUADRA: {combQuadra}')
    print(f'\nProbabilidades de Acertos\nSENA: 1/{len(lstCombinacoes)} = {(1 / len(lstCombinacoes))*100:.5f} %.')
    print(f'QUINA: {combQuina}/{len(lstCombinacoes)} = {(combQuina / len(lstCombinacoes))*100:.5f} %.')
    print(f'QUADRA: {combQuadra}/{len(lstCombinacoes)} = {(combQuadra / len(lstCombinacoes))*100:.5f} %.\n')