strTexto = """O sol se ergue sobre o campo da Gália, e com ele as hostes gaulesas de Vercingetórix
se preparam para enfrentar-nos. Contudo, a vitória será nossa não pela força bruta, mas pela
astúcia e pela disciplina das legiões romanas. Como é de nosso costume, a mente hábil será
mais poderosa que a lâmina afiada. O inimigo, embora numeroso e bem posicionado, comete o erro
de subestimar a flexibilidade de nossas formações. Ele acredita que o flanco esquerdo de seu
exército é seguro. E é exatamente aí que vejo a oportunidade de esmagá-lo. Ordeno, portanto, que
tu, Marco Antônio, tomes o comando das nossas tropas e as posicione ao longo do flanco esquerdo
de Vercingetórix. Sei que o terreno é difícil, coberto de arbustos e com diversas elevações, mas
é essa falsa confiança do inimigo que nos dará a vantagem. Ele acreditará que aquela região está
fora de alcance, e, por isso, não dará a devida atenção à sua proteção. Esse erro será nossa
armadilha. O movimento que desejo que faças não é de ataque direto, mas uma manobra que o engane.
Quando o inimigo perceber a movimentação, ele se verá forçado a reagir, provavelmente desviando
parte de suas forças para aquele flanco, o que causará a desorganização de suas linhas. Nossa
vantagem, então, será dar-lhe a falsa sensação de que estamos atacando um ponto crucial, enquanto
preparamos o golpe real. Com a reorganização do inimigo, será o momento de agir. Nossas legiões,
disciplinadas e ávidas pela vitória, devem então se lançar com toda a força, aproveitando a brecha
que criamos. Vercingetórix não terá tempo de reagir adequadamente, e sua confiança será sua própria
ruína. Não te esqueças, Marco Antônio, que a guerra não é vencida apenas com espada e escudo, mas
com mente e vontade. A verdadeira força está em manter a ordem e a estratégia firmes diante do caos.
Confio em ti, como sempre, para executar este movimento com precisão e destreza. Que as legiões
romanas, com sua disciplina e coragem, avancem para a vitória. Que tu estejas em posição para
realizar a tarefa, pois o momento da ação se aproxima Ave César"""

strCaracteres = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzáàâãäåçéèêíìîóòôõöúùûüÁÀÂÃÄÅÇÉÈÊÍÌÎÓÒÔÕÖÚÙÛÜ0123456789 !\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~'''
#chaveAleatoria = 'vigenere'
strCriptografada = ''
strCriptografadaChaveada = ''
strCriptografadaNova = ''
strCriptografadaChaveadaNova = ''
indiceCripto = 0 

#print(f'Texto original:\n{strTexto}\n')

# criptografar com a primeira chave
chaveCripto = ''
for letra in range(len(strTexto[-9:])):
    print(letra, end='; ')
    letraTemp = strCaracteres.find(strTexto[letra])
    print(letraTemp, end='; ')
    alfabetoTemp = strCaracteres[letraTemp:] + strCaracteres[:letraTemp]
    print(alfabetoTemp)
    chaveCripto += alfabetoTemp[strCaracteres.find(strCaracteres[letraTemp])]

'''for letra in range(len(strTexto)):
    if indiceCripto == len(chaveAleatoria): indiceCripto = 0
    strCriptografada += chaveAleatoria[indiceCripto]
    indiceCripto += 1
    if letra + 1 == len(strTexto): indiceCripto = 0'''

#print(f'Texto criptografado com primeira chave:\n{strCriptografada}\n')
print(f'Primeira chave:\n{chaveCripto}\n')

# criar alfabeto cifrado
for letra in range(len(strTexto)): # usando range(), pois strTexto e strCriptografada tem o mesmo tam
    letraTemporaria = strCaracteres.find(strTexto[letra])
    strAlfabeto = strCaracteres[letraTemporaria:] + strCaracteres[:letraTemporaria]

    strTemporaria = strAlfabeto[strCaracteres.find(strCriptografada[letra])]
    strCriptografadaChaveada += strTemporaria

chaveNova = strCriptografadaChaveada[-9:]

print(f'Texto criptografado 1:\n{strCriptografadaChaveada}\n')

# criptografar com a segunda (nova) chave
for letra in range(len(strCriptografadaChaveada)):
    if indiceCripto == len(chaveNova): indiceCripto = 0
    strCriptografadaNova += chaveNova[indiceCripto]
    indiceCripto += 1
    if letra + 1 == len(strCriptografadaChaveada): indiceCripto = 0

print(f'Texto criptografado com nova chave:\n{strCriptografadaNova}\n')

# usando a chave nova em strTexto
for letra in range(len(strCriptografadaNova)):
    letraTemporaria = strCaracteres.find(strTexto[letra])
    strAlfabeto = strCaracteres[letraTemporaria:] + strCaracteres[:letraTemporaria]

    strTemporaria = strAlfabeto[strCaracteres.find(strCriptografadaNova[letra])]
    strCriptografadaChaveadaNova += strTemporaria

print(f'Criptografia com Nova chave:\n{strCriptografadaChaveadaNova}\n')