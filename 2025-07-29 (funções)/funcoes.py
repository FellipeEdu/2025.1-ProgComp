def mediaIFRN(nota1:int, nota2:int) -> int:

    if not isinstance(nota1, int):
        raise ValueError('Informe Nota 1 inteiro')
    if not isinstance(nota2, int):
        raise ValueError('Informe Nota 2 inteiro')

    if nota1 < 0 or nota1 > 100:
        raise Exception ('Nota 1 deve ser entre 0 e 100')
    if nota2 < 0 or nota2 > 100:
        raise Exception ('Nota 2 deve ser entre 0 e 100')

    media = (nota1 * 2 + nota2 * 3) / 5
    return int(round(media, 0))