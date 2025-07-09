import os

# diretorio
strDir = os.path.dirname(__file__)

try:
    arqLeitura = open(f'{strDir}\\times.csv', 'r', encoding='utf-8')

except FileNotFoundError:
    print('ERRO: Arquivo não encontrado.')

except Exception as excecao:
    print(f'ERRO: {excecao}.')

else:
    lstTimes = list()

    while True:
        # Lendo a linha e armazenando na variavel
        strLinha = arqLeitura.readline().strip()

        # interrompe o laço quando nao ha conteudo na linha (EOF)
        if not strLinha: break

        # transforma string em lista
        #lstAux = strLinha.split(';')
        lstAux = [int(i) if i.isdigit() else i for i in strLinha.split(';')]

        # add dados na lst
        lstTimes.append(lstAux)
    arqLeitura.close()

print(lstTimes)