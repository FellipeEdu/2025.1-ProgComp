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
        # para cada linha do arquivo txt (incluindo o '\n') ele vai imprimir os '-'
        print('-' * 80)
        print(strConteudo.strip())

    arqLeitura.close()