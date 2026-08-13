'''
Sistema de Vidas e Penalidade 
Criar a variável vidas = 3. Se o inimigo encostar na nave perde 1 de vida.
'''

# Import
import turtle
import math #faz calculos
import random #sorteia numeros pseudoaleatórios
from PIL import Image
import pygame

# --- SISTEMA DE ÁUDIO (EFEITOS SONOROS E MÚSICA TEMA) ---
pygame.mixer.init()  # Inicializa o sistema de som do Pygame

try:
    som_tiro = pygame.mixer.Sound("sons/laser.mp3")  # Carrega o efeito sonoro do laser/tiro
except pygame.error:
    print("Aviso: Arquivo 'tiro.mp3' não encontrado. O jogo seguirá sem som de tiro.")  # Mensagem de aviso
    som_tiro = None  # Marca que não há som de tiro disponível

try:
    som_gameover = pygame.mixer.Sound("sons/gameover.mp3")  # Carrega o efeito sonoro de Game Over
except pygame.error:
    print("Aviso: Arquivo 'gameover.wav' não encontrado. O jogo seguirá sem som de Game Over.")  # Mensagem de aviso
    som_gameover = None  # Marca que não há som de Game Over disponível

Image.MAX_IMAGE_PIXELS = None
LARGURA = 800
ALTURA = 600

# Janela
janela = turtle.Screen()
janela.title("Gamezinho")
janela.bgpic("gif/espaco.gif")
janela.bgcolor("black")
janela.setup(width=LARGURA, height=ALTURA)
janela.tracer(0)


#estrelas mechendo em parallax
estrelas = []  # Lista que vai guardar todos os objetos de estrelas
for _ in range(50):  # Cria 50 estrelas para o fundo
    estrela = turtle.Turtle()  # Cria um novo objeto Turtle para a estrela
    estrela.shape("circle")  # Define a forma da estrela como um círculo
    estrela.color("white")  # Define a cor da estrela como branca
    estrela.penup()  # Desativa o rastro da caneta
    tam = random.uniform(0.05, 0.25)  # Gera um tamanho aleatório para dar sensação de profundidade
    estrela.shapesize(stretch_wid=tam, stretch_len=tam)  # Aplica o tamanho na estrela
    estrela.velocidade = tam * 7  # Define a velocidade com base no tamanho (Efeito Parallax)
    
    # IMPORTANTE: X usa LARGURA e Y usa ALTURA
    estrela.goto(random.randint(-LARGURA // 2 + 10, LARGURA // 2 - 10),  # Posiciona a estrela em X aleatório
                 random.randint(-ALTURA // 2 + 20, ALTURA // 2 - 20))  # Posiciona a estrela em Y aleatório
    estrelas.append(estrela)  # Adiciona a estrela criada na lista de estrelas

#nave
nave = turtle.Turtle()
janela.addshape("gif/nave.gif")
nave.shape("gif/nave.gif")
nave.color("#cb85f3")
nave.penup() #não deixa linha
nave.setheading(90) #apontando pra cima
nave.goto(0, -240) #posição


#inimigo
inimigo = turtle.Turtle()
janela.addshape("gif/pedra.gif")
inimigo.shape("gif/pedra.gif")
inimigo.penup()
inimigo.goto(random.randint(-360, 360), 280) # o X é aleatório, de -360 a 360, o Y é 280
inimigo_vel = 0.3

#laser
laser = turtle.Turtle()
janela.addshape("gif/laser.gif")
laser.shape("gif/laser.gif")
laser.color("pink")
laser.shapesize(stretch_wid=1, stretch_len=0.2)
laser.penup()
laser.hideturtle() #esconde
laser_vel = 3
laser_estado = "pronto"

#placar
pontosf = 0
pontos = 0
placar = turtle.Turtle()
placar.speed(0)
placar.color("#8d4387")
placar.penup()
placar.hideturtle()
placar.goto(-340, 230)
placar.write(f"Pontos: {pontos}", align="left", font=("Impact", 20, "normal")) # escreve

#vidas
vida = 3
vidas = turtle.Turtle()
vidas.speed(0)
vidas.color("#8d4387")
vidas.penup()
vidas.hideturtle()
vidas.goto(-340, 200)
vidas.write(f"Vidas: {vida}", align="left", font=("Impact", 20, "normal"))

#fases
fase = 1
fases = turtle.Turtle()
fases.speed(0)
fases.color("#8d4387")
fases.penup()
fases.hideturtle()
fases.goto(-340, 170)
fases.write(f"Fase: {fase}", align="left", font=("Impact", 20, "normal"))

#movimentos
def vaiEsquerda():
    if nave.xcor() > -370: #limite borda esquerda
        nave.setx(nave.xcor() - 20)

def vaiDireita():
    if nave.xcor() < 370: #limite borda direita
        nave.setx(nave.xcor() + 20)

def vaiCima():
    if nave.ycor() < 240: #limite borda cima
        nave.sety(nave.ycor() + 20)

def vaiBaixo():
    if nave.ycor() > -240: #limite borda baixo
        nave.sety(nave.ycor() - 20)

def vaiLaser():
    global laser_estado
    if laser_estado == "pronto":
        laser_estado = "disparado"
        laser.goto(nave.xcor(), nave.ycor()+10)
        laser.showturtle() #mostra
        if som_tiro:
            som_tiro.play()


#mapear teclas
janela.listen() #"Ouvir o teclado"

janela.onkeypress(vaiEsquerda, "a")
janela.onkeypress(vaiDireita, "d")
janela.onkeypress(vaiCima, "w")
janela.onkeypress(vaiBaixo, "s")

janela.onkeypress(vaiEsquerda, "Left")
janela.onkeypress(vaiDireita, "Right")
janela.onkeypress(vaiCima, "Up")
janela.onkeypress(vaiBaixo, "Down")

janela.onkeypress(vaiLaser, "space")

# game loop: inicia a janela, faz o inimigo ir descendo a tela, se o inimigo chegar la na borda 
# de baixo, ele volta pro topo, se o laser estiver disparado, ele vai indo pra cima, quando ele passar 
# do topo, ele recarrega, se o laser atingir o inimigo ele some.

while True:
    janela.update() #forçar o sistema a atualizar a janela imediatamente. 
    p = 0
    for estrela in estrelas:  # Para cada estrela da lista
    # Altera o eixo Y (vertical) subtraindo a velocidade para ir para baixo
        estrela.sety(estrela.ycor() - estrela.velocidade)  
        
        # Se a estrela sair da tela pela borda inferior (baixo)
        if estrela.ycor() < -ALTURA // 2:  
            # Reposiciona no topo (ALTURA // 2) com um X (horizontal) aleatório
            estrela.goto(random.randint(-LARGURA // 2 + 10, LARGURA // 2 - 10), ALTURA // 2)


    inimigo.sety(inimigo.ycor() - inimigo_vel)
    if inimigo.ycor() < -290:
        inimigo.goto(random.randint(-360, 360), 280)
    if laser_estado == "disparado":
        laser.sety(laser.ycor() + laser_vel)

        if laser.ycor() > 290:
            laser.hideturtle()
            laser_estado = "pronto"

        distancia = math.sqrt((laser.xcor() - inimigo.xcor()) ** 2 + (laser.ycor() - inimigo.ycor())**2)
                
        if distancia < 20:
            laser.hideturtle()
            laser_estado = "pronto"
            inimigo.goto(random.randint(-360, 360), 280)

            #Pontuação
            pontos += 1
            pontosf+=1
            #fases
            if pontos == 5 and fase == 1:
                fase+=1
                inimigo_vel += 0.25
                pontos = 0
                fases.clear()
                fases.write(f"Fase: {fase}", align="left", font=("Impact", 20, "normal"))
                placar.clear()
                placar.write(f"Pontos: {pontos}", align="left", font=("Impact", 20, "normal"))

            elif pontos == 10 and fase == 2:
                fase+=1
                inimigo_vel += 0.25
                pontos = 0
                fases.clear()
                fases.write(f"Fase: {fase}", align="left", font=("Impact", 20, "normal"))
                placar.clear()
                placar.write(f"Pontos: {pontos}", align="left", font=("Impact", 20, "normal"))

            elif pontos == 15 and fase == 3:
                fase+=1
                inimigo_vel += 0.25
                pontos = 0
                fases.clear()
                fases.write(f"Fase: {fase}", align="left", font=("Impact", 20, "normal"))
                placar.clear()
                placar.write(f"Pontos: {pontos}", align="left", font=("Impact", 20, "normal"))

            elif pontos == 20 and fase == 4:
                p = pontos
                fase+=1
                inimigo_vel += 0.25
                pontos = 0
                fases.clear()
                fases.write(f"Fase: {fase}", align="left", font=("Impact", 20, "normal"))
                placar.clear()
                placar.write(f"Pontos: {pontos}", align="left", font=("Impact", 20, "normal"))
                

            elif pontos-5 == p and fase == 5:
                inimigo_vel += 0.3
                p = pontos
                fases.clear()
                fases.write(f"Fase: {fase}", align="left", font=("Impact", 20, "normal"))
                placar.clear()
                placar.write(f"Pontos: {pontos}", align="left", font=("Impact", 20, "normal"))
            
            placar.clear()
            placar.write(f"Pontos: {pontos}", align="left", font=("Impact", 20, "normal"))
            
    dInimigo = math.sqrt((nave.xcor() - inimigo.xcor()) ** 2 + (nave.ycor() - inimigo.ycor())**2)
    if dInimigo < 20:
        vida -= 1
        vidas.clear()
        vidas.write(f"Vidas: {vida}", align="left", font=("Impact", 20, "normal"))
        inimigo.goto(random.randint(-360, 360), 280)
        
        if vida <= 0:
            vidas.clear() 
            nave.hideturtle()
            laser.hideturtle()
            inimigo.hideturtle()
            vidas.hideturtle()
            fases.hideturtle()
            

            pygame.mixer.music.stop()  # Interrompe a música tema
            if som_gameover:  # Se o som de Game Over foi carregado com sucesso
                som_gameover.play()  # Toca o efeito sonoro de Game Over

            #Game Over
            fim = turtle.Turtle()
            fim.shape("blank") # <-- CORREÇÃO: Remove o formato de triângulo padrão do Turtle
            fim.speed(0)
            fim.color("#8d4387")
            fim.penup()
            fim.hideturtle()
            fim.goto(0, 0)
            fim.write(f"GAME OVER", align="center", font=("Impact", 80, "normal")) # escreve

            fim.showturtle()
            placar.clear() # Limpa o placar lá do topo da tela
            placar.goto(0, -40) # Coloca o placar um pouco abaixo do Game Over
            placar.write(f"Pontuação Final: {pontosf}", align="center", font=("Impact", 24, "normal"))
            fases.clear() # Limpa o placar lá do topo da tela
            fases.goto(0, -70) # Coloca o placar um pouco abaixo do Game Over
            fases.write(f"Fase: {fase}", align="center", font=("Impact", 24, "normal"))

            janela.update()
            break # Sai do loop do jogo

# Mantém a janela aberta aguardando a ação de fechar do usuário
janela.mainloop()
