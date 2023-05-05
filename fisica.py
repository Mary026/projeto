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
print(lista_X)

#Armazenar os dados do tempo da bola
#lista_T = []
#arquivo_T = open("TempoBola.txt", "r")
#leitura_do_arquivo_T = arquivo_T.readlines()
#for linha_arquivo_T in leitura_do_arquivo_T:
#    arquivo_T.close()
#    separacao_T = float(linha_arquivo_T[:-1])
#    lista_T.append(separacao_T)
#print(lista_T)

#Quadrantes - 1 Quadrante
y_inicial_1 = 3.0
y_final_1 = 5.3
x_inicial_1 = 4.5
x_final_1 = 9.0

#Quadrantes - 2 Quadrante

#Quadrantes - 3 Quadrante
#Quadrantes - 4 Quadrante
#Analisando qual posição da bola estará mais perto do robô em Y
for posicao_mais_perto_y in lista_Y:
    if posicao_mais_perto_y < robo_y:
        posicao_y = posicao_mais_perto_y
print(posicao_y)

for indice_Y in range(len(lista_Y)):
    if lista_Y[indice_Y] == posicao_y:
        indice_Y = indice_Y
        print(indice_Y)
        break

for indice_X in range(len(lista_X)):
    indice_X = indice_Y
    print(indice_X)
    break

#posicao_x = 

#distancia_robo_e_bola = (((robo_x - posicao_x)**2) + ((robo_y - posicao_y)**2))
#distancia_robo_e_bola = sqrt(distancia_robo_e_bola)
#print(distancia_robo_e_bola)



#!!!