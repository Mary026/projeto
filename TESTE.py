from math import *
from tkinter import *
import matplotlib.pyplot as plt


def calcular():
    #Inputs para a posição do robô em X e Y
    robo_x = float(entry_x.get())
    robo_y = float(entry_y.get())

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
    lista_T = []
    arquivo_T = open("TempoBola.txt", "r")
    leitura_do_arquivo_T = arquivo_T.readlines()
    for linha_arquivo_T in leitura_do_arquivo_T:
        arquivo_T.close()
        separacao_T = float(linha_arquivo_T[:-1])
        lista_T.append(separacao_T)

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
    indice_T = indice_X
    for t in range(indice_T):
        tempo_bola = lista_T[t]
    print("Tempo da bola quando está na posição determinada mais próxima do robô: %.2f\n" % tempo_bola)

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
    tempo_robo_cheguei = tempo_robo_cheguei * 1000
    print(tempo_robo_cheguei)
    print(" ")

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
        distancia_ate_o_gol = sqrt(distancia_ate_o_gol)
        distancia_ate_o_gol = round(distancia_ate_o_gol, 3)
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

    # Força de atrito cinetico
    forca_atrito_cinetico = 0.5 * robo_peso
    forca_atrito_cinetico = round(forca_atrito_cinetico, 3)
    print("A força de atrito cinético que o robô vai realizar sobre a bola: %.3f\n" % forca_atrito_cinetico)

    # Força de atrito estatico
    forca_atrito_estatico = 0.7 * robo_peso
    forca_atrito_estatico = round(forca_atrito_estatico, 3)
    print("A força de atrito estático que o robô vai realizar sobre a bola: %.3f\n" % forca_atrito_estatico)

    # Trabalho realizado
    trabalho_realizado = (forca + forca_atrito_cinetico - forca_atrito_estatico) * distancia_ate_o_gol
    trabalho_realizado = round(trabalho_realizado, 3)
    print("O trabalho que o robô vai realizar: %.3f\n" % trabalho_realizado)
    
    # Contas para os gráficos
    # Distância da origem até a bola interceptada
    distancia_bola = (((posicao_x)**2) + ((posicao_y)**2))
    distancia_bola = sqrt(distancia_bola)
    distancia_bola = round(distancia_bola, 3)
    print("A distância da origem até a bola: %.3f\n" % distancia_bola)

    # Distância incial
    distancia_bola_incial = (((1.010)**2) + ((0.508)**2))
    distancia_bola_incial = sqrt(distancia_bola_incial)
    distancia_bola_incial = round(distancia_bola_incial, 3)
    print("A distância da origem até o primeiro ponto da bola: %.3f\n" % distancia_bola_incial)
    
    # Velocidade média inicial da bola
    v0_bola = distancia_bola_incial / 0.02
    print("A distância da origem até o primeiro ponto da bola: %.3f\n" % v0_bola)
    
    # Ângulo da bola
    angulo_bola = 0.508 / 1.010
    angulo_bola = atan(angulo_bola)
    
    # Conversão de ângulos
    cosseno = cos(angulo_bola)
    seno = sin(angulo_bola)

    cosseno = round(cosseno, 3)
    seno = round(seno, 3)

    # Trajetória da bola x em função de x
    v0x_bola = v0_bola * cosseno
    print("A velocidade de v0x: %.3f\n" % v0x_bola)
    #xt = 1.000 + v0x_bola * tempo

    # Gráfico 1 (Gráfico das trajetórias da bola e do robô em um plano 𝑥𝑦, até o ponto de interceptação)
def plot_intersecao(robot_x_inicial, robot_y_inicial, robot_x_final, robot_y_final,
                    ball_x_inicial, ball_y_inicial, ball_x_final, ball_y_final):
    # Configurar o gráfico
    fig, ax = plt.subplots()

    # Traçar a rota do robô
    ax.plot([robot_x_inicial, robot_x_final], [robot_y_inicial, robot_y_final], 'r-', label='Rota do Robô')

    # Traçar a rota da bola
    ax.plot([ball_x_inicial, ball_x_final], [ball_y_inicial, ball_y_final], 'b-', label='Rota da Bola')

    # Adicionar ponto inicial e final do robô
    ax.plot(robot_x_inicial, robot_y_inicial, 'go', label='Início do Robô')
    ax.plot(robot_x_final, robot_y_final, 'go', color='red', label='Fim do Robô')

    # Adicionar ponto inicial e final da bola
    #ax.plot(ball_x_inicial, ball_y_inicial, 'bo', label='Início da Bola')
    #ax.plot(ball_x_final, ball_y_final, 'bo', label='Fim da Bola')

    # Definir os limites do gráfico
    ax.set_xlim(min(robot_x_inicial, robot_x_final, ball_x_inicial, ball_x_final) - 1,
                max(robot_x_inicial, robot_x_final, ball_x_inicial, ball_x_final) + 1)
    ax.set_ylim(min(robot_y_inicial, robot_y_final, ball_y_inicial, ball_y_final) - 1,
                max(robot_y_inicial, robot_y_final, ball_y_inicial, ball_y_final) + 1)

    # Adicionar rótulos e legenda
    ax.set_xlabel('Coordenada X')
    ax.set_ylabel('Coordenada Y')
    ax.legend()

    # Mostrar o gráfico
    plt.show()

    # Exemplo de uso
    robot_x_inicial = 6.660
    robot_y_inicial = 5.261
    robot_x_final = 8.855
    robot_y_final = 5.260
    ball_x_inicial = 1.000
    ball_y_inicial = 0.500
    ball_x_final = 9.000
    ball_y_final = 5.300

    plot_intersecao(robot_x_inicial, robot_y_inicial, robot_x_final, robot_y_final,
                    ball_x_inicial, ball_y_inicial, ball_x_final, ball_y_final)
    # Gráfico 2
    # Gráfico 3
    # Gráfico 4
    # Gráfico 5

    result_label.configure(text="Distância que o robô terá que percorrer: %.3f" % distancia_robo_e_bola)

root = Tk()
root.title("Cálculo de Distância do Robô")

frame = Frame(root)
frame.pack(pady=20)

label_x = Label(frame, text="Posição do robô em X:")
label_x.grid(row=0, column=0)
entry_x = Entry(frame)
entry_x.grid(row=0, column=1)

label_y = Label(frame, text="Posição do robô em Y:")
label_y.grid(row=1, column=0)
entry_y = Entry(frame)
entry_y.grid(row=1, column=1)

calculate_button = Button(root, text="Calcular", command=calcular)
calculate_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
