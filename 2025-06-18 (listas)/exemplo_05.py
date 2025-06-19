lstAlunos = list()
lstNotas_1 = list()
lstNotas_2 = list()

while True:
    strNome = input('Digite um nome: ').strip()

    if strNome.lower() == 'fim': 
        break
    
    # TO DO: quando ocorrer algum erro nas notas o programa deve voltar para pedir a partir das notas
    try:
        intNota_1 = int(input('Digite a nota 1: '))
        intNota_2 = int(input('Digite a nota 2: '))
    except ValueError:
        print('ERRO: Informe um inteiro válido.')
    except Exception as e:
        print(f'ERRO: {e}')
    else:
        if intNota_1 < 0 and intNota_1 > 100:
            print('ERRO: Nota inválida. Informe entre 0 e 100')
        elif intNota_2 < 0 and intNota_2 > 100:
            print('ERRO: Nota inválida. Informe entre 0 e 100')
        else:
            # TO DO: add o nome e as notas dos alunos apenas na lista lstAlunos
            lstAlunos.append(strNome)
            lstNotas_1.append(intNota_1)
            lstNotas_2.append(intNota_2)
            # TO DO: add em cada aluno a media, seguindo a formula do IFRN

print(lstAlunos)
print(lstNotas_1)
print(lstNotas_2)