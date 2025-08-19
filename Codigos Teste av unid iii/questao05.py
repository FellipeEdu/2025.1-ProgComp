import os, sys

diretorio = os.path.dirname(__file__)

try:
    gabLeitura = open(f'{diretorio}\\gabarito.txt', 'r', encoding='utf-8')
    provasLeitura = open(f'{diretorio}\\provas.csv', 'r', encoding='utf-8')
    arqEscrita = open(f'{diretorio}\\RESULTADOS.csv', 'w', encoding='utf-8')
except FileNotFoundError:
    sys.exit('\nERRO: Arquivo não encontrado...')
except Exception as erro:
    sys.exit(f'\nERRO: {erro}')
else:
    lstGabarito = list(gabLeitura.readline().split())
    lstProvas = list()

    while True:
        strProva = provasLeitura.readline().strip()
        if not strProva: break
        lstAux = [linha for linha in strProva.split(';')]
        lstProvas.append(lstAux)

    provasLeitura.close()
    gabLeitura.close()

    # inserindo notas
    for prova in lstProvas:
        acertos = 0
        for nota in range(1, len(prova)): # começa de [1] pois [0] é o nome do aluno
            if prova[nota] == lstGabarito[nota - 1]: acertos += 1
            else: continue
        prova.append(acertos)

    lstProvas.sort(key=lambda prova: prova[11], reverse=True)
    
    for prova in lstProvas:
        linha = '; '.join(str(i) for i in prova)
        arqEscrita.write(f'{linha}\n')
    arqEscrita.close()

    for prova in lstProvas: print(prova)