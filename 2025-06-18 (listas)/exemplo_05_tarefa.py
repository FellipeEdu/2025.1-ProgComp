lstAlunos = list()
lstNotas_1 = list()
lstNotas_2 = list()

while True:
    strNome = input('Digite um nome: ').strip()
    intNota_1 = None
    intNota_2 = None

    if strNome.lower() == 'fim': 
        break
    
    # TO DO: quando ocorrer algum erro nas notas o programa deve voltar para pedir a partir das notas
    while intNota_1 == None or intNota_2 == None:
        try:
            intNota_1 = int(input('Digite a nota 1: '))
            intNota_2 = int(input('Digite a nota 2: '))
        except ValueError:
            print('ERRO: Informe um inteiro válido.')
        except Exception as e:
            print(f'ERRO: {e}')
        else:
            if intNota_1 < 0 or intNota_1 > 100:
                print('ERRO: Nota inválida. Informe entre 0 e 100')
                intNota_1 = None # atribui None à intNota pra retornar para o while antes do try

            elif intNota_2 < 0 or intNota_2 > 100:
                print('ERRO: Nota inválida. Informe entre 0 e 100')
                intNota_2 = None # atribui None à intNota pra retornar para o while antes do try
                
            else:
                # TO DO: add o nome e as notas dos alunos apenas na lista lstAlunos
                lstAlunos.append(strNome)
                #lstNotas_1.append(intNota_1)
                #lstNotas_2.append(intNota_2)

                lstAlunos.append(intNota_1)
                lstAlunos.append(intNota_2)
                # TO DO: add em cada aluno a media, seguindo a formula do IFRN
                media_IF = int(((intNota_1 * 2) + (intNota_2 * 3)) / 5)
                lstAlunos.append(media_IF)

print(lstAlunos)
#print(lstNotas_1)
#print(lstNotas_2)