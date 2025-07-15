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
        # retirando os traços (-) e '\n' a mais que estavam sendo gerados em cada paragrafo
        strConteudo = strConteudo.strip()
        if strConteudo: print('\n' + '-'*80)
        print(strConteudo, end='')

    arqLeitura.close()