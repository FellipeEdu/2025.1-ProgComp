import os, sys, json

strDirApp = os.path.dirname(__file__)

strNomeArq = f'{strDirApp}//cartola_fc_2024.json'

try:
    arqInput = open(strNomeArq, 'r',encoding='utf-8')
    strDados = arqInput.read()
    # transformando em dicionario
    dictCartola = json.loads(strDados)
    arqInput.close()

except FileNotFoundError:
    sys.exit('ERRO: Arquivo não existe.')
except json.JSONDecodeError:
    sys.exit('ERRO: o conteúdo do arquivo não está no formato correto.')
except Exception as erro:
    sys.exit(f'ERRO: {erro}.')
else:
    lstChaves = list(dictCartola.keys()) # ['clubes', 'posicoes', 'status', 'atletas']

    '''
        dictCartola = {'clubes': {...}, 'posicoes': {...}, 'status': {...}, 'atletas': {...} }

        dictCartola['clubes']   -> dicionário (k:v)
        dictCartola['posicoes'] -> dicionário (k:v)
        dictCartola['status']   -> dicionário (k:v)
        dictCartola['atletas']  -> lista (índice -> dicionário (k:v))
    '''
    # Informando o nome do clube
    strNomeClube = input('\nInforme o nome do Clube: ').strip().lower() 
    
    # Obtendo o ID do clube informado (fazendo filtragem pela chave nome_fantasia)

    # Listando os atletas do Clube informado

    '''
    lstAux = dictCartola['clubes']
    
    #print(lstChaves)

    print(lstAux)

    # conteudo de cada chave
    #print(dictCartola['atletas'])

finally:
    print('\nFIM DO PROGRAMA...')'''