import sys, os

diretorio = os.path.dirname(__file__)

try:
    arqLeitura = open(f'{diretorio}\\alunos_ifrn.csv', 'r', encoding='utf-8')
    escritaCampus = open(f'{diretorio}\\ALUNOS_IFRN_CAMPUS.csv', 'w', encoding='utf-8')
    escritaAlunos = open(f'{diretorio}\\ALUNOS_IFRN_ANO.csv', 'w', encoding='utf-8')
except FileNotFoundError:
    sys.exit('\nERRO: arquivo não encontrado.')
except Exception as excecao:
    sys.exit(f'\nERRO: {excecao}')
else:
    lstCampus = list()
    lstAnos = list()
    lstCursos = list()
    while True:
        strLinha = arqLeitura.readline().strip()
        if not strLinha: break
        lstAux = [linha for linha in strLinha.split(';')]
        # preenchendo lstCampus (evita pegar o nome 'campus' do header)
        if len(lstAux[10]) < 6: lstCampus.append(lstAux[10])
        # preenchendo lstAnos contando apenas 1 aluno pois ha alunos com mais de uma matricula
        if lstAux[7][:4] < '2025' and lstAux[7][:4] > '1990': lstAnos.append(lstAux[7][:4])
        # preenchendo lstCursos
        lstCursos.append([lstAux[10], lstAux[5]])

    # item 1
    lstCampus.sort()
    lstCampusEstat = list()
    contAlunos = 0
    for alunos in range(len(lstCampus)):
        if alunos + 1 < len(lstCampus) and lstCampus[alunos] == lstCampus[alunos + 1]:
            contAlunos += 1
        else:
            # add campus e quant de alunos com porcentagem
            lstCampusEstat.append([lstCampus[alunos], contAlunos + 1, str(round((contAlunos / len(lstCampus)) * 100, 2)) + ' %'])
            contAlunos = 0
    lstCampusEstat.sort(key=lambda alunos: alunos[1], reverse=True)

    escritaCampus.write('Campus; Quant. de Alunos; % em relação ao total\n')
    for campus in lstCampusEstat:
        linha = '; '.join(str(i) for i in campus)
        escritaCampus.write(f'{linha}\n')
    escritaCampus.close()
    print("\nArquivo 'ALUNOS_IFRN_CAMPUS.csv' criado com sucesso.")

    # item 2
    lstAnos.sort()
    lstAnosEstat = list()
    contAlunosAno = 0
    for alunos in range(len(lstAnos)):
        if alunos + 1 < len(lstAnos) and lstAnos[alunos] == lstAnos[alunos + 1]:
            contAlunosAno += 1
        else:
            # add ano e quant de alunos
            lstAnosEstat.append([lstAnos[alunos], contAlunosAno + 1])
            contAlunosAno = 0
    lstAnosEstat.sort(key=lambda alunos: alunos[1], reverse=True)

    escritaAlunos.write('Ano de entrada; Quant. de Alunos\n')
    for aluno in lstAnosEstat:
        linha = '; '.join(str(i) for i in aluno)
        escritaAlunos.write(f'{linha}\n')
    escritaAlunos.close()
    print("\nArquivo 'ALUNOS_IFRN_ANO.csv' criado com sucesso.")

    # item 3
    outraConsulta = None
    while not outraConsulta == 'N':
        escritaCursos = open(f'{diretorio}\\ALUNOS_IFRN_CAMPUS_CURSO.csv', 'w', encoding='utf-8')

        print('\nDigite a sigla do Campus para visualizar os cursos.')
        sigla = input('[CNAT, MO, ZL, CN, CA, NC, ZN, CAL, SGA, IP, MC, PAR, SC,\nJC, PF, AP, CANG, SPP, CM, LAJ, PAAS]: ').upper()
        while not sigla in lstCampus:
            sigla = input('\nERRO: digite uma sigla válida.\nDigite a sigla: ').upper()

        lstCursosTemp = list(filter(lambda campus:campus[0] == sigla, lstCursos))
        lstCursosTemp.sort()
        lstCursosEstat = list()
        contAlunosCurso = 0
        for alunos in range(len(lstCursosTemp)):
            if alunos + 1 < len(lstCursosTemp) and lstCursosTemp[alunos] == lstCursosTemp[alunos + 1]:
                contAlunosCurso += 1
            else:
                # add cursos e quant de alunos
                lstCursosEstat.append([lstCursosTemp[alunos][1], contAlunosCurso + 1])
                contAlunosCurso = 0
        lstCursosEstat.sort(key=lambda alunos: alunos[1], reverse=True)

        escritaCursos.write('Curso; Quant. de Alunos\n')
        for aluno in lstCursosEstat:
            linha = '; '.join(str(i) for i in aluno)
            escritaCursos.write(f'{linha}\n')
        escritaCursos.close()
        print("\nArquivo 'ALUNOS_IFRN_CAMPUS_CURSO.csv' criado com sucesso.")

        outraConsulta = input('\nDeseja visualizar de novo?\nSim [S] ou Não [N]: ').upper()
        while not (outraConsulta == 'S' or outraConsulta == 'N'):
            outraConsulta = input('\nERRO: digite um valor válido.\nDeseja visualizar de novo? ').upper()