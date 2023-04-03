lista_Y = []
arquivo = open("PosicaoBolaEmY.txt", "r")
leitura_do_arquivo_Y = arquivo.readlines()
for linha_arquivo_Y in leitura_do_arquivo_Y:
    arquivo.close()
    separacao_Y = float(linha_arquivo_Y[:-2])
    lista_Y.append(separacao_Y)
print(lista_Y)
