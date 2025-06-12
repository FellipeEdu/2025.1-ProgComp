strPalavra = input('Digite a palavra desejada: ')
intDeslocamento = int(input('Deslocamento Desejado: '))

strCifra = ''

for contador in range(0, len(strPalavra) + 1):
    strCifra += chr(ord(strPalavra[0]) + intDeslocamento)