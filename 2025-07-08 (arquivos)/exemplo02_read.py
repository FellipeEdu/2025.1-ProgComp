import os

strDir = os.path.dirname(__file__)

try:
    arqLeitura = open(f'{strDir}\\carta.txt', 'r', encoding='utf-8')

except FileNotFoundError:
    print('ERRO: Arquivo não encontrado.')

except Exception as excecao:
    print(f'ERRO: {excecao}.')

else:
    strConteudo = arqLeitura.read()

    arqLeitura.close()

    print(strConteudo)