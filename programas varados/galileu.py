import random
try:
    print("Termo: Adivinhe a palavra de 5 digitos")
    palavrasaleatorias = ["pleno", "risco", "claro", "trago", "forte", "vento", "chave", "basta", "nuvem", "saiba", "lente", "mente", "copos", "brisa", "tocar"] # As palavras aleatorias

    amarelo = '\033[1;33m'
    vermelho = "\033[0;31m"
    verde = '\033[0;32m'
    padrao = '\033[0m'

    letras = ''

    segredo1 = random.randint(0, len(palavrasaleatorias) - 1).upper() # Escolher a primeira palavra secreta
    segredo2 = random.randint(0, len(palavrasaleatorias) - 1).upper() # Escolher a segunda palavra secreta

    while segredo1 == segredo2: # Garantir que as palavras sejam diferentes
        segredo2 = random.randint(0, len(palavrasaleatorias) - 1).upper()

    adivinhar = input("Adivinhe a palavra secreta: ").upper()
    tentativas = 0
    ntemletra = []

    while tentativas <= 7:
        adivinhar = input("Adivinhe a palavra secreta: ").upper()

        if len(adivinhar) != 5:
            print("A palavra deve ter 5 letras!")
            continue

        for pos_adivinha in range(len(adivinhar)):

            if adivinhar[pos_adivinha] == segredo1[pos_adivinha] and segredo2[pos_adivinha]:
                letras = letras + verde + adivinhar[pos_adivinha] + padrao + ''

            if adivinhar[pos_adivinha] in segredo1[pos_adivinha] and segredo2[pos_adivinha]:
                letras = letras + amarelo + adivinhar[pos_adivinha] + padrao + ''

            if adivinhar[pos_adivinha] not in segredo1[pos_adivinha] and segredo2[pos_adivinha]:
                letras = letras + vermelho + adivinhar[pos_adivinha] + padrao + ''
                if adivinhar[pos_adivinha] not in ntemletra:
                    ntemletra.append(letras)

        print(f"As letras que já foram usadas e não pertencem {sorted(ntemletra)}")
        print(letras)

        tentativas += 1
    if adivinhar == segredo1 and segredo2:
        print(f'Você acertou as duas palavras do dia! ')

except ValueError as val:
    print("Você digitou um número onde era para ser uma letra! ", val)
except Exception as e:
    print("Houve um erro inesperado!", e)