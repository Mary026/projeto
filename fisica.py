from math import *
#Inputs para a posição do robô em X e Y
robo_x = float(input("Digite a posição do robô em X: "))
robo_y = float(input("Digite a posição do robô em Y: "))

#Valores que utilizaremos para o robô
robo_velocidade = 2.78
robo_aceleracao = 2.78
robo_peso = 2.78

#Armazenar os dados da bola na Posição Y do plano cartesiano em uma lista
lista_Y = []
arquivo_Y = open("PosicaoBolaEmY.txt", "r")
leitura_do_arquivo_Y = arquivo_Y.readlines()
for linha_arquivo_Y in leitura_do_arquivo_Y:
    arquivo_Y.close()
    separacao_Y = float(linha_arquivo_Y[:-1])
    lista_Y.append(separacao_Y)

#Armazenar os dados da bola na Posição X do plano cartesiano em uma lista
lista_X = []
arquivo_X = open("PosicaoBolaEmX.txt", "r")
leitura_do_arquivo_X = arquivo_X.readlines()
for linha_arquivo_X in leitura_do_arquivo_X:
    arquivo_X.close()
    separacao_X = float(linha_arquivo_X[:-1])
    lista_X.append(separacao_X)

#Armazenar os dados do tempo da bola
#lista_T = []
#arquivo_T = open("TempoBola.txt", "r")
#leitura_do_arquivo_T = arquivo_T.readlines()
#for linha_arquivo_T in leitura_do_arquivo_T:
#    arquivo_T.close()
#    separacao_T = float(linha_arquivo_T[:-1])
#    lista_T.append(separacao_T)
#print(lista_T)

#Analisando qual posição da bola estará mais perto do robô em Y
for posicao_mais_perto_y in lista_Y:
    if posicao_mais_perto_y < robo_y:
        posicao_y = posicao_mais_perto_y
print(posicao_y)

# Descobrindo o indice da lista Y e lista X
for indice_Y in range(len(lista_Y)):
    if lista_Y[indice_Y] == posicao_y:
        indice_Y = indice_Y + 1
        print(indice_Y)
        break
indice_X = indice_Y
print(indice_X)

# Descobrindo o valor da lista X no indice
for x in range(indice_X):
    posicao_x = lista_X[x]
print(posicao_x)

# Descobrindo o valor da lista T no indice
#indice_T = indice_X
#for t in range(indice_T):
#    tempo_bola = lista_T[t]
#print(tempo_bola)

# Cálculo da distância do robô até a bola 
distancia_robo_e_bola = (((robo_x - posicao_x)**2) + ((robo_y - posicao_y)**2))
distancia_robo_e_bola = sqrt(distancia_robo_e_bola)
distancia_robo_e_bola = round(distancia_robo_e_bola, 3)
print(distancia_robo_e_bola)

# Raio de Interceptação
distancia_robo_e_bola = distancia_robo_e_bola - 0.01

# Tempo em que o robô vai demorar para chegar na bola
tempo_robo_cheguei = distancia_robo_e_bola/robo_velocidade
tempo_robo_cheguei = round(tempo_robo_cheguei, 2)
print(tempo_robo_cheguei)

# Descobrindo em qual quadrante a bola está
if (robo_x > 4.5 and robo_x < 9.0) and (robo_y > 3.0 and robo_y < 6.0):
    print("O ROBÔ ESTÁ NO PRIMEIRO QUADRANTE")
    if (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 3.0 and posicao_y < 6.0):
        print("A BOLA ESTÁ NO PRIMEIRO QUADRANTE")
    elif (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 3.0 and posicao_y < 6.0):
        print("A BOLA ESTÁ NO SEGUNDO QUADRANTE")
    elif (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 0 and posicao_y < 3.0):
        print("A BOLA ESTÁ NO TERCEIRO QUADRANTE")
    elif (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 0 and posicao_y < 3.5):
        print("A BOLA ESTÁ NO QUARTO QUADRANTE")
    else:
        print("A BOLA NÃO ESTÁ NO CAMPO")

if (robo_x > 0 and robo_x < 4.5) and (robo_y > 3.0 and robo_y < 6.0):
    print("O ROBÔ ESTÁ NO SEGUNDO QUADRANTE")
    if (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 3.0 and robo_y < 6.0):
        print("A BOLA ESTÁ NO PRIMEIRO QUADRANTE")
    elif (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 3.0 and posicao_y < 6.0):
        print("A BOLA ESTÁ NO SEGUNDO QUADRANTE")
    elif (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 0 and posicao_y < 3.0):
        print("A BOLA ESTÁ NO TERCEIRO QUADRANTE")
    elif (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 0 and posicao_y < 3.5):
        print("A BOLA ESTÁ NO QUARTO QUADRANTE")
    else:
        print("A BOLA NÃO ESTÁ NO CAMPO")

if (robo_x > 0 and robo_x < 4.5) and (robo_y > 0 and robo_y < 3.0):
    print("O ROBÔ ESTÁ NO TERCEIRO QUADRANTE")
    if (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 3.0 and robo_y < 6.0):
        print("A BOLA ESTÁ NO PRIMEIRO QUADRANTE")
    elif (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 3.0 and posicao_y < 6.0):
        print("A BOLA ESTÁ NO SEGUNDO QUADRANTE")
    elif (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 0 and posicao_y < 3.0):
        print("A BOLA ESTÁ NO TERCEIRO QUADRANTE")
    elif (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 0 and posicao_y < 3.5):
        print("A BOLA ESTÁ NO QUARTO QUADRANTE")
    else:
        print("A BOLA NÃO ESTÁ NO CAMPO")

if (robo_x > 4.5 and robo_x < 9.0) and (robo_y > 0 and robo_y < 3.5):
    print("O ROBÔ ESTÁ NO QUARTO QUADRANTE")
    if (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 3.0 and robo_y < 6.0):
        print("A BOLA ESTÁ NO PRIMEIRO QUADRANTE")
    elif (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 3.0 and posicao_y < 6.0):
        print("A BOLA ESTÁ NO SEGUNDO QUADRANTE")
    elif (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 0 and posicao_y < 3.0):
        print("A BOLA ESTÁ NO TERCEIRO QUADRANTE")
    elif (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 0 and posicao_y < 3.5):
        print("A BOLA ESTÁ NO QUARTO QUADRANTE")
    else:
        print("A BOLA NÃO ESTÁ NO CAMPO")
