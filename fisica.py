from math import *
#Inputs para a posição do robô em X e Y
robo_x = float(input("Digite a posição do robô em X: "))
robo_y = float(input("Digite a posição do robô em Y: "))

#Valores que utilizaremos para o robô
robo_velocidade = 2.78
robo_aceleracao = 2.78
robo_peso = 2.78
robo_massa = 0.278

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
print("Posição da bola mais perto do robô: %.3f\n" % posicao_y)

# Descobrindo o indice da lista Y e lista X
for indice_Y in range(len(lista_Y)):
    if lista_Y[indice_Y] == posicao_y:
        indice_Y = indice_Y + 1
        print("Indíce da lista da posição da bola em Y: %d\n" % indice_Y)
        break
indice_X = indice_Y
print("Indíce da lista da posição da bola em Y: %d\n" % indice_X)

# Descobrindo o valor da lista X no indice
for x in range(indice_X):
    posicao_x = lista_X[x]
print("Posição da bola em X quando ela tem o valor anterior em Y: %.3f\n" % posicao_x)

# Descobrindo o valor da lista T no indice
#indice_T = indice_X
#for t in range(indice_T):
#    tempo_bola = lista_T[t]
#print("Tempo da bola quando está na posição determinada mais próxima do robô: %.2f\n" % tempo_bola)

# Cálculo da distância do robô até a bola 
distancia_robo_e_bola = (((posicao_x - robo_x)**2) + ((posicao_y - robo_y)**2))
distancia_robo_e_bola = sqrt(distancia_robo_e_bola)
distancia_robo_e_bola = round(distancia_robo_e_bola, 3)
print("A distância que o robô terá que percorrer sem o raio de interceptação: %.3f\n" % distancia_robo_e_bola)

# Raio de Interceptação
distancia_robo_e_bola = distancia_robo_e_bola - 0.11
print("A distância que o robô terá que percorrer com o raio de interceptação: %.3f\n" % distancia_robo_e_bola)

# Tempo em que o robô vai demorar para chegar na bola
tempo_robo_cheguei = distancia_robo_e_bola/robo_velocidade
tempo_robo_cheguei = round(tempo_robo_cheguei, 2)
print("Tempo que o robô vai demorar para chegar na bola: %.2f\n" % tempo_robo_cheguei)

# Conversão de segundo para milissegundo
# tempo_robo_cheguei = tempo_robo_cheguei * 1000
# print(tempo_robo_cheguei)

# Descobrindo em qual quadrante o robô e a bola estão
# Robô no primeiro quadrante
if (robo_x > 4.5 and robo_x < 9.0) and (robo_y > 3.0 and robo_y < 6.0):
    print("O ROBÔ ESTÁ NO PRIMEIRO QUADRANTE\n")
    if (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 3.0 and posicao_y < 6.0):
        print("A BOLA ESTÁ NO PRIMEIRO QUADRANTE\n")
        print("ESTÁ MAIS PERTO DO GOL DA DIREITA\n")
    elif (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 3.0 and posicao_y < 6.0):
        print("A BOLA ESTÁ NO SEGUNDO QUADRANTE\n")
        print("ESTÁ MAIS PERTO DO GOL DA ESQUERDA\n")
    elif (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 0 and posicao_y < 3.0):
        print("A BOLA ESTÁ NO TERCEIRO QUADRANTE\n")
        print("ESTÁ MAIS PERTO DO GOL DA ESQUERDA\n")
    elif (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 0 and posicao_y < 3.5):
        print("A BOLA ESTÁ NO QUARTO QUADRANTE\n")
        print("ESTÁ MAIS PERTO DO GOL DA DIREITA\n")
    else:
        print("A BOLA NÃO ESTÁ NO CAMPO\n")

# Robô no segundo quadrante
if (robo_x > 0 and robo_x < 4.5) and (robo_y > 3.0 and robo_y < 6.0):
    print("O ROBÔ ESTÁ NO SEGUNDO QUADRANTE\n")
    if (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 3.0 and robo_y < 6.0):
        print("A BOLA ESTÁ NO PRIMEIRO QUADRANTE\n")
        print("ESTÁ MAIS PERTO DO GOL DA DIREITA\n")
    elif (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 3.0 and posicao_y < 6.0):
        print("A BOLA ESTÁ NO SEGUNDO QUADRANTE\n")
        print("ESTÁ MAIS PERTO DO GOL DA ESQUERDA\n")
    elif (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 0 and posicao_y < 3.0):
        print("A BOLA ESTÁ NO TERCEIRO QUADRANTE\n")
        print("ESTÁ MAIS PERTO DO GOL DA ESQUERDA\n")
    elif (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 0 and posicao_y < 3.5):
        print("A BOLA ESTÁ NO QUARTO QUADRANTE\n")
        print("ESTÁ MAIS PERTO DO GOL DA DIREITA\n")
    else:
        print("A BOLA NÃO ESTÁ NO CAMPO\n")

# Robô no terceiro quadrante
if (robo_x > 0 and robo_x < 4.5) and (robo_y > 0 and robo_y < 3.0):
    print("O ROBÔ ESTÁ NO TERCEIRO QUADRANTE\n")
    if (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 3.0 and robo_y < 6.0):
        print("A BOLA ESTÁ NO PRIMEIRO QUADRANTE\n")
        print("ESTÁ MAIS PERTO DO GOL DA DIREITA\n")
    elif (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 3.0 and posicao_y < 6.0):
        print("A BOLA ESTÁ NO SEGUNDO QUADRANTE\n")
        print("ESTÁ MAIS PERTO DO GOL DA ESQUERDA\n")
    elif (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 0 and posicao_y < 3.0):
        print("A BOLA ESTÁ NO TERCEIRO QUADRANTE\n")
        print("ESTÁ MAIS PERTO DO GOL DA ESQUERDA\n")
    elif (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 0 and posicao_y < 3.5):
        print("A BOLA ESTÁ NO QUARTO QUADRANTE\n")
        print("ESTÁ MAIS PERTO DO GOL DA DIREITA\n")
    else:
        print("A BOLA NÃO ESTÁ NO CAMPO\n")

# Robô no quarto quadrante
if (robo_x > 4.5 and robo_x < 9.0) and (robo_y > 0 and robo_y < 3.5):
    print("O ROBÔ ESTÁ NO QUARTO QUADRANTE\n")
    if (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 3.0 and robo_y < 6.0):
        print("A BOLA ESTÁ NO PRIMEIRO QUADRANTE\n")
        print("ESTÁ MAIS PERTO DO GOL DA DIREITA\n")
    elif (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 3.0 and posicao_y < 6.0):
        print("A BOLA ESTÁ NO SEGUNDO QUADRANTE\n")
        print("ESTÁ MAIS PERTO DO GOL DA ESQUERDA\n")
    elif (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 0 and posicao_y < 3.0):
        print("A BOLA ESTÁ NO TERCEIRO QUADRANTE\n")
        print("ESTÁ MAIS PERTO DO GOL DA ESQUERDA\n")
    elif (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 0 and posicao_y < 3.5):
        print("A BOLA ESTÁ NO QUARTO QUADRANTE\n")
        print("ESTÁ MAIS PERTO DO GOL DA DIREITA\n")
    else:
        print("A BOLA NÃO ESTÁ NO CAMPO\n")

# Cálculo para chegar no gol (GOL DA ESQUERDA)
if ((posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 3.0 and posicao_y < 6.0) or (posicao_x > 0 and posicao_x < 4.5) and (posicao_y > 0 and posicao_y < 3.0)):
    distancia_ate_o_gol = (((0.5 - posicao_x)**2) + ((3 - posicao_y)**2))
    distancia_ate_o_gol = sqrt(distancia_robo_e_bola)
    distancia_ate_o_gol = round(distancia_robo_e_bola, 3)
    print("A distância que o robô terá que percorrer para chegar até o gol da esquerda com a bola: %.3f\n" % distancia_ate_o_gol)

# Cálculo para chegar no gol (GOL DA DIREITA)
if ((posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 0 and posicao_y < 3.0) or (posicao_x > 4.5 and posicao_x < 9.0) and (posicao_y > 3.0 and robo_y < 6.0)):
    distancia_ate_o_gol = (((8.5 - posicao_x)**2) + ((3 - posicao_y)**2))
    distancia_ate_o_gol = sqrt(distancia_ate_o_gol)
    distancia_ate_o_gol = round(distancia_ate_o_gol, 3)
    print("A distância que o robô terá que percorrer para chegar até o gol da direita com a bola: %.3f\n" % distancia_ate_o_gol)

# Força que ele vai ter que fazer
forca = robo_massa * robo_aceleracao
forca = round(forca, 3)
print("A força que o robô vai realizar sobre a bola: %.3f\n" % forca)

# Trabalho realizado
trabalho_realizado = forca * distancia_ate_o_gol
trabalho_realizado = round(trabalho_realizado, 3)
print("O trabalho que o robô vai realizar: %.3f\n" % trabalho_realizado)

#Teste