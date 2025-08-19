import sys, os

diretorio = os.path.dirname(__file__)

outraConsulta = None
print('----- CONSULTA CENSO IBGE -----')
while not outraConsulta == 'N':
    try:
        arqLeitura = open(f'{diretorio}\\censo_2022_populacao_residente_municipios.csv', 'r', encoding='utf-8-sig')
        entrada = int(input('Por Região [1] Por Estado [2]: '))

        while not (entrada == 1 or entrada == 2):
            print('\nERRO: digite apenas 1 ou 2.')
            entrada = int(input('Por Região [1] Por Estado [2]: '))
    except ValueError:
        print('\nERRO: informe um valor válido.')
    except Exception as excecao:
        sys.exit(f'\nERRO: {excecao}')
    else:
        lstCenso = list()
        lstCabecalho = arqLeitura.readline().strip().split(';')
        while True:
            strLinha = arqLeitura.readline().strip()
            if not strLinha: break
            lstAux = [linha for linha in strLinha.split(';')]
            populacao = int(lstAux[3])
            lstCenso.append([lstAux[0], lstAux[1], lstAux[2], populacao])

        # por regiao 
        if entrada == 1:
            lstEstados = list()
            regiao = int(input('Digite a Região desejada:\nNorte [1],  Nordeste [2], Centro-Oeste [3], Sudeste [4], Sul [5]: '))
            while not (regiao == 1 or regiao == 2 or regiao == 3 or regiao == 4 or regiao == 5):
                print('\nERRO: digite um valor válido.')
                regiao = int(input('Digite a Região desejada:\nNorte [1],  Nordeste [2], Centro-Oeste [3], Sudeste [4], Sul [5]: ')) 
            if regiao == 1: lstEstados = ['AM', 'AC', 'RR', 'RO', 'PA', 'AP', 'TO']
            elif regiao == 2: lstEstados = ['AL', 'BA', 'CE', 'MA', 'RN', 'PB', 'PE', 'SE', 'PI']
            elif regiao == 3: lstEstados = ['DF', 'GO', 'MS', 'MT']
            elif regiao == 4: lstEstados = ['MG', 'ES', 'SP', 'RJ']
            elif regiao == 5: lstEstados = ['PR', 'SC', 'RS']

            lstEstadosRegiao = [[i[0], i[2], i[3]] for i in lstCenso if i[2] in lstEstados]
            lstEstadosRegiao.sort(key=lambda municipio: municipio[2], reverse=True)

            print(f'\n{'Municípios':<25} ... {'Estado'} ... {'População'}')
            for mun in lstEstadosRegiao[:10]: 
                print(f'{mun[0]:<25} ... {mun[1]:<6} ... {mun[2]}')
        # por estado
        elif entrada == 2:
            lstTodosEstados = [estado[2] for estado in lstCenso]
            estado = input('Digite a sigla (Ex.: RN) do estado desejado: ').upper()
            while not estado in lstTodosEstados:
                print('\nERRO: digite um estado existente.')
                estado = input('Digite a sigla (Ex.: RN) do estado desejado: ').upper()

            lstEstadosCidades = [[i[0], i[2], i[3]] for i in lstCenso if i[2] == estado]
            lstEstadosCidades.sort(key=lambda populacao: populacao[2], reverse=True)

            print(f'\n{'Municípios':<25} ... {'Estado'} ... {'População'}')
            for mun in lstEstadosCidades[:10]:
                print(f'{mun[0]:<25} ... {mun[1]:<6} ... {mun[2]}')

        outraConsulta = input('\nDeseja fazer outra consulta?\nSim [S] ou Não [N]: ').upper()
        while not (outraConsulta == 'S' or outraConsulta == 'N'):
            print('\nERRO: digite um valor válido.')
            outraConsulta = input('Deseja fazer outra consulta?\nSim [S] ou Não [N]: ').upper()
arqLeitura.close()
print('\n----- FIM DO PROGRAMA -----')