x = float(input("Digite a posição do robô em X: "))
y = float(input("Digite a posição do robô em Y: "))


lista_Y = []
arquivo_Y = open("PosicaoBolaEmY.txt", "r")
leitura_do_arquivo_Y = arquivo_Y.readlines()
for linha_arquivo_Y in leitura_do_arquivo_Y:
    arquivo_Y.close()
    separacao_Y = float(linha_arquivo_Y[:-2])
    lista_Y.append(separacao_Y)
print(lista_Y)

lista_X = []
arquivo_X = open("PosicaoBolaEmX.txt", "r")
leitura_do_arquivo_X = arquivo_X.readlines()
for linha_arquivo_X in leitura_do_arquivo_X:
    arquivo_X.close()
    separacao_X = float(linha_arquivo_X[:-2])
    lista_X.append(separacao_X)
print(lista_X)