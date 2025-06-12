strPalavra = input('Digite a palavra desejada: ')
intDeslocamento = int(input('Deslocamento Desejado: '))

strCifra = ''

print(f'Cifra com deslocamento {intDeslocamento}: ', end='')

for contador in range(0, len(strPalavra)):

    intCorrecao = 0
    intString = ord(strPalavra[contador]) + intDeslocamento

    if (intString) > 126:
        intCorrecao = (intString - 127) + 33
        strCifra = chr(intCorrecao)
    else:
        strCifra = chr(intString)

    print(strCifra, end='')