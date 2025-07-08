try:
    arqLeitura = open('carta.txt', 'r')

except FileNotFoundError:
    print('ERRO: Arquivo não encontrado.')

except Exception as excecao:
    print(f'ERRO: {excecao}.')
    
else:
    strConteudo = arqLeitura.readlines()

    arqLeitura.close()

    print(strConteudo)