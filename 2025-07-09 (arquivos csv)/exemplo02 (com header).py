import os

# diretorio
strDir = os.path.dirname(__file__)

try:
    arqLeitura = open(f'{strDir}\\times_header.csv', 'r', encoding='utf-8')

except FileNotFoundError:
    print('ERRO: Arquivo não encontrado.')

except Exception as excecao:
    print(f'ERRO: {excecao}.')

else:
    lstTimes = list()
    lstCabecalho = list()

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

# add pontuacao e saldo de gols
for time in lstTimes:
    time.insert(4, time[1]*3 + time[2])
    time.append(time[5] - time[6])

#
lstCabecalho.insert(4, 'Pontuação')
lstCabecalho.append('Saldo de Gols')

# classificando os times
lstTimes.sort(key=lambda time: (time[4], time[1], time[7], time[5]), reverse=True)

print(lstCabecalho)
for time in lstTimes:
    print(time)