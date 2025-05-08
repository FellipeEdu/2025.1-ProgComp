import sys

etapa1 = int(input('informe a nota da etpaa 1: '))

if etapa1 < 0 or etapa1 > 100:
    sys.exit('ERRO: nota etapa 1 invalida. Informe nota entre 0 e 100')    

etapa2 = int(input('informe a nota da etpaa 2: '))

if etapa2 < 0 or etapa2 > 100:
    sys.exit('ERRO: nota etapa 2 invalida. Informe nota entre 0 e 100')

media = round((etapa1 * 2 + etapa2 * 3) / 5, 0) # arredondando media no calculo
print(f'Media do aluno: {media}') # verificando a media sem arredondar na formatação
print(f'Media do aluno: {media:.0f}')

if media >= 60:
    print('Aluno Aprovado.')
elif media >= 20:
    print('Aluno em Prova Final.')
else:
    print('Aluno Reprovado.') 