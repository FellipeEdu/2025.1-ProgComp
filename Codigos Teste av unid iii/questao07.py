import sys, os

diretorio = os.path.dirname(__file__)

try:
    arqLeitura = open(f'{diretorio}\\produtos_informatica.csv.csv', 'r', encoding='utf-8')
    arqEscrita = open(f'{diretorio}\\RESULTADO_LICITACAO.CSV', 'w', encoding='utf-8')
except FileNotFoundError:
    sys.exit('\nERRO: arquivo não encontrado.')
except Exception as excecao:
    sys.exit(f'\nERRO: {excecao}')
else:
    lstCabecalho = arqLeitura.readline().strip().split(';')
    lstProdutos = list()
    lstProdDesconto = list()
    while True:
        strLinha = arqLeitura.readline().strip()
        if not strLinha: break
        lstAux = strLinha.split(';')
        lstProdutos.append([lstAux[0], lstAux[1], float(lstAux[2]), float(lstAux[3]), float(lstAux[4])])
    
    lstEmpresas = [2, 3, 4] # A, B, C
    empresa = int(input('Empresa desejada para a consulta (Empresa A - 1; Empresa B - 2, Empresa C - 3): ')) + 1
    while not empresa in lstEmpresas: empresa = int(input('ERRO: digite uma empresa entre as listadas\nEmpresa desejada: ')) + 1
    desconto = float(input('Desconto a ser aplicado (em %): ')) / 100  

    lstProdDesconto = list(map(lambda prod:[prod[0], prod[1], prod[2] * (1 - desconto) if empresa == 2 else prod[2],
                                            prod[3] * (1 - desconto) if empresa == 3 else prod[3],
                                            prod[4] * (1 - desconto) if empresa == 4 else prod[4]], lstProdutos))
    
    # add produto, categoria, melhor preco, melhor empresa
    lstMelhorPreco = list(map(lambda prod:[prod[0], prod[1], f'{min(prod[2:]):.2f}', lstCabecalho[prod[2:].index(min(prod[2:])) + 2]], lstProdDesconto))

    arqEscrita.write(f'{lstCabecalho[0]};{lstCabecalho[1]};Melhor Preço;Empresa\n')
    for prod in lstMelhorPreco:
        linha = ';'.join(str(i) for i in prod)
        arqEscrita.write(f'{linha}\n')
    arqEscrita.close()
    print("Arquivo 'RESULTADO_LICITACAO.CSV' criado com sucesso.\n")
    #for prod in lstMelhorPreco: print(prod)