def mediaIFRN(nota1:int, nota2:int) -> int:

    if not isinstance(nota1, int):
        raise ValueError('argumento \'Nota 1\' deve ser do tipo INT')
    if not isinstance(nota2, int):
        raise ValueError('argumento \'Nota 2\' deve ser do tipo INT')

    if nota1 < 0 or nota1 > 100:
        raise Exception ('Nota 1 deve ser entre 0 e 100')
    if nota2 < 0 or nota2 > 100:
        raise Exception ('Nota 2 deve ser entre 0 e 100')

    media = (nota1 * 2 + nota2 * 3) / 5
    return int(round(media, 0))

def situacaoFinal(media:int) -> str:

    if not isinstance(media, int): raise ValueError('argumento \'media\' deve ser do tipo INT')

    if media >= 60: situacao = 'Aprovado !'
    elif media >= 20: situacao = 'Prova Final !'
    else: situacao = 'REPROVADO !'

    return situacao

def mediaIFRN_v3(nota1:int, nota2:int) -> int:
    # Verificando se os argumentos informados são do tipo INT e 
    # estão entre 0 e 100
    for nota, nome in [(nota1, 'nota1'), (nota2, 'nota2')]:
        if not isinstance(nota, int):
            raise ValueError(f'O argumento \'{nome}\' deve ser do tipo INT')
        if nota < 0 or nota > 100:
            raise Exception(f'O argumento \'{nome}\' deve ser entre 0 e 100')
        
    # Calculando a média
    media = int(round((nota1*2 + nota2*3)/5,0))
    
    # Obtendo a situação final do aluno
    situacao = situacaoFinal(media)

    # Retornando o valor da média ao programa
    return (media, situacao)