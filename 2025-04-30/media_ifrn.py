# Calcular media da disciplina do IFRN
#
# 1) solicitar ao usuario que informe suas notas 
# 2) calcular a media do IFRN 
# 3) Exibir a media
#
# Media = ((Etapa1 * 2) + (Etapa2 * 3)) / 5

etapa_1 = int(input('digite nota 1: '))
etapa_2 = int(input('digite nota 2: '))

media = ((etapa_1 * 2) + (etapa_2 * 3)) / 5

print(f'sua media: {media:.0f}')