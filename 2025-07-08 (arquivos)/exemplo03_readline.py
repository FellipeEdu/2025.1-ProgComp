import os

strDir = os.path.dirname(__file__)

try:
    arqLeitura = open(f'{strDir}\\carta.txt', 'r', encoding='utf-8')

except FileNotFoundError:
    print('ERRO: Arquivo não encontrado.')

except Exception as excecao:
    print(f'ERRO: {excecao}.')

else:
    '''strConteudo = arqLeitura.read()

    arqLeitura.close()

    print(strConteudo)'''

    while True:
        strConteudo = arqLeitura.readline()
        if not strConteudo: break
        #print(strConteudo)
        print('=' * 80)
        print(strConteudo.strip())

    arqLeitura.close()