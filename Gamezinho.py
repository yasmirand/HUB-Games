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
    print("Aviso: Arquivo 'tiro.mp3' não encontrado. O jogo seguirá sem som de tiro.")
    som_tiro = None

try:
    som_gameover = pygame.mixer.Sound("sons/gameover.mp3")  # Carrega o efeito sonoro de Game Over
except pygame.error:
    print("Aviso: Arquivo 'gameover.wav' não encontrado. O jogo seguirá sem som de Game Over.")
    som_gameover = None

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


# estrelas mechendo em parallax
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
    estrela.goto(
        random.randint(-LARGURA // 2 + 10, LARGURA // 2 - 10),
        random.randint(-ALTURA // 2 + 20, ALTURA // 2 - 20)
    )
    estrelas.append(estrela)  # Adiciona a estrela criada na lista de estrelas


# nave
nave = turtle.Turtle()
janela.addshape("gif/nave.gif")
nave.shape("gif/nave.gif")
nave.color("#cb85f3")
nave.penup() #não deixa linha
nave.setheading(90) #apontando pra cima
nave.goto(0, -240) #posição


# inimigo
inimigo = turtle.Turtle()
janela.addshape("gif/pedra.gif")
inimigo.shape("gif/pedra.gif")
inimigo.penup()
inimigo.goto(random.randint(-360, 360), 280)
inimigo_vel = 0.3


# laser
laser = turtle.Turtle()
janela.addshape("gif/laser.gif")
laser.shape("gif/laser.gif")
laser.color("pink")
laser.shapesize(stretch_wid=1, stretch_len=0.2)
laser.penup()
laser.hideturtle()
laser_vel = 10
laser_estado = "pronto"


# placar
pontosf = 0
pontos = 0
placar = turtle.Turtle()
placar.speed(0)
placar.color("#8d4387")
placar.penup()
placar.hideturtle()
placar.goto(-340, 230)
placar.write(
    f"Pontos: {pontos}",
    align="left",
    font=("Impact", 20, "normal")
)


# vidas
vida = 3
vidas = turtle.Turtle()
vidas.speed(0)
vidas.color("#8d4387")
vidas.penup()
vidas.hideturtle()
vidas.goto(-340, 200)
vidas.write(
    f"Vidas: {vida}",
    align="left",
    font=("Impact", 20, "normal")
)


# fases
fase = 1
fases = turtle.Turtle()
fases.speed(0)
fases.color("#8d4387")
fases.penup()
fases.hideturtle()
fases.goto(-340, 170)
fases.write(
    f"Fase: {fase}",
    align="left",
    font=("Impact", 20, "normal")
)


texto_anuncio = turtle.Turtle()
texto_anuncio.speed(0)
texto_anuncio.color("#8d4387")
texto_anuncio.penup()
texto_anuncio.hideturtle()


# ==========================================================
# NOVO: ESTADO DO JOGO
# ==========================================================

estado_jogo = "JOGANDO"


# ==========================================================
# movimentos
# ==========================================================

def vaiEsquerda():
    if estado_jogo == "JOGANDO":
        if nave.xcor() > -370:
            nave.setx(nave.xcor() - 20)


def vaiDireita():
    if estado_jogo == "JOGANDO":
        if nave.xcor() < 370:
            nave.setx(nave.xcor() + 20)


def vaiCima():
    if estado_jogo == "JOGANDO":
        if nave.ycor() < 240:
            nave.sety(nave.ycor() + 20)


def vaiBaixo():
    if estado_jogo == "JOGANDO":
        if nave.ycor() > -240:
            nave.sety(nave.ycor() - 20)


def vaiLaser():
    global laser_estado

    if estado_jogo == "JOGANDO":
        if laser_estado == "pronto":
            laser_estado = "disparado"
            laser.goto(nave.xcor(), nave.ycor() + 10)
            laser.showturtle()

            if som_tiro:
                som_tiro.play()


# ==========================================================
# NOVO: FUNÇÃO DE REINICIAR
# ==========================================================

def reiniciar_jogo():
    global pontosf
    global pontos
    global vida
    global fase
    global inimigo_vel
    global laser_estado
    global estado_jogo

    # Só reinicia se estiver no Game Over
    if estado_jogo == "GAMEOVER":

        # Reseta os valores
        pontosf = 0
        pontos = 0
        vida = 3
        fase = 1
        inimigo_vel = 0.3
        laser_estado = "pronto"

        # Reseta o estado
        estado_jogo = "JOGANDO"
        fim.clear()
        # Reseta posições
        nave.goto(0, -240)
        inimigo.goto(random.randint(-360, 360), 280)

        # Mostra novamente os objetos
        nave.showturtle()
        inimigo.showturtle()

        # Esconde o laser
        laser.hideturtle()
        laser.goto(0, -1000)

        # Limpa os textos de Game Over
        texto_anuncio.clear()

        # Volta os placares para a posição original
        placar.goto(-340, 230)
        placar.clear()
        placar.write(
            f"Pontos: {pontos}",
            align="left",
            font=("Impact", 20, "normal")
        )

        vidas.goto(-340, 200)
        vidas.clear()
        vidas.write(
            f"Vidas: {vida}",
            align="left",
            font=("Impact", 20, "normal")
        )

        fases.goto(-340, 170)
        fases.clear()
        fases.write(
            f"Fase: {fase}",
            align="left",
            font=("Impact", 20, "normal")
        )

        # Reinicia a música, caso ela esteja sendo usada
        try:
            pygame.mixer.music.play(-1)
        except pygame.error:
            pass


# ==========================================================
# mapear teclas
# ==========================================================

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


# ==========================================================
# NOVO: TECLA R PARA REINICIAR
# ==========================================================

janela.onkeypress(reiniciar_jogo, "r")
janela.onkeypress(reiniciar_jogo, "R")


# ==========================================================
# game loop
# ==========================================================

while True:

    janela.update()

    # ======================================================
    # ESTRELAS
    # Elas continuam se mexendo mesmo no Game Over
    # ======================================================

    for estrela in estrelas:

        estrela.sety(estrela.ycor() - estrela.velocidade)

        if estrela.ycor() < -ALTURA // 2:
            estrela.goto(
                random.randint(-LARGURA // 2 + 10, LARGURA // 2 - 10),
                ALTURA // 2
            )


    # ======================================================
    # NOVO:
    # Só executa a lógica do jogo se estiver jogando
    # ======================================================

    if estado_jogo == "JOGANDO":

        # --------------------------------------------------
        # inimigo
        # --------------------------------------------------

        inimigo.sety(inimigo.ycor() - inimigo_vel)

        if inimigo.ycor() < -290:
            inimigo.goto(
                random.randint(-360, 360),
                280
            )


        # --------------------------------------------------
        # laser
        # --------------------------------------------------

        if laser_estado == "disparado":

            laser.sety(laser.ycor() + laser_vel)

            if laser.ycor() > 290:
                laser.hideturtle()
                laser_estado = "pronto"


            # --------------------------------------------------
            # colisão laser x inimigo
            # --------------------------------------------------

            distancia = math.sqrt(
                (laser.xcor() - inimigo.xcor()) ** 2 +
                (laser.ycor() - inimigo.ycor()) ** 2
            )

            if distancia < 20:

                laser.hideturtle()
                laser_estado = "pronto"

                inimigo.goto(
                    random.randint(-360, 360),
                    280
                )

                # Pontuação
                pontos += 1
                pontosf += 1


                # --------------------------------------------------
                # fases
                # --------------------------------------------------

                if pontos == 5 and fase == 1:

                    fase += 1
                    inimigo_vel += 0.5
                    pontos = 0

                    fases.clear()
                    fases.write(
                        f"Fase: {fase}",
                        align="left",
                        font=("Impact", 20, "normal")
                    )

                    placar.clear()
                    placar.write(
                        f"Pontos: {pontos}",
                        align="left",
                        font=("Impact", 20, "normal")
                    )


                elif pontos == 10 and fase == 2:

                    fase += 1
                    inimigo_vel += 0.5
                    pontos = 0

                    fases.clear()
                    fases.write(
                        f"Fase: {fase}",
                        align="left",
                        font=("Impact", 20, "normal")
                    )

                    placar.clear()
                    placar.write(
                        f"Pontos: {pontos}",
                        align="left",
                        font=("Impact", 20, "normal")
                    )


                elif pontos == 15 and fase == 3:

                    fase += 1
                    inimigo_vel += 0.5
                    pontos = 0

                    fases.clear()
                    fases.write(
                        f"Fase: {fase}",
                        align="left",
                        font=("Impact", 20, "normal")
                    )

                    placar.clear()
                    placar.write(
                        f"Pontos: {pontos}",
                        align="left",
                        font=("Impact", 20, "normal")
                    )
                elif pontos == 20 and fase == 4:

                    p = pontos
                    fase += 1
                    inimigo_vel += 0.5
                    pontos = 0

                    fases.clear()
                    fases.write(
                        f"Fase: {fase}",
                        align="left",
                        font=("Impact", 20, "normal")
                    )

                    placar.clear()
                    placar.write(
                        f"Pontos: {pontos}",
                        align="left",
                        font=("Impact", 20, "normal")
                    )
                elif pontos - 5 == pontosf and fase == 5:

                    inimigo_vel += 0.5
                    p = pontos

                    fases.clear()
                    fases.write(
                        f"Fase: {fase}",
                        align="left",
                        font=("Impact", 20, "normal")
                    )

                    placar.clear()
                    placar.write(
                        f"Pontos: {pontos}",
                        align="left",
                        font=("Impact", 20, "normal")
                    )


                placar.clear()
                placar.write(
                    f"Pontos: {pontos}",
                    align="left",
                    font=("Impact", 20, "normal")
                )


        # ==================================================
        # colisão inimigo x nave
        # ==================================================

        dInimigo = math.sqrt(
            (nave.xcor() - inimigo.xcor()) ** 2 +
            (nave.ycor() - inimigo.ycor()) ** 2
        )

        if dInimigo < 20:

            vida -= 1

            vidas.clear()
            vidas.write(
                f"Vidas: {vida}",
                align="left",
                font=("Impact", 20, "normal")
            )

            inimigo.goto(
                random.randint(-360, 360),
                280
            )


            # ==================================================
            # GAME OVER
            # ==================================================

            if vida <= 0:

                # NOVO: muda o estado em vez de dar break
                estado_jogo = "GAMEOVER"

                # Esconde os objetos
                nave.hideturtle()
                laser.hideturtle()
                inimigo.hideturtle()

                vidas.clear()
                vidas.hideturtle()
                fases.hideturtle()


                # Para a música
                pygame.mixer.music.stop()

                if som_gameover:
                    som_gameover.play()


                # Game Over
                fim = turtle.Turtle()
                fim.shape("blank")
                fim.speed(0)
                fim.color("#8d4387")
                fim.penup()
                fim.hideturtle()
                fim.goto(0, 0)

                fim.write(
                    "GAME OVER",
                    align="center",
                    font=("Impact", 80, "normal")
                )

                fim.showturtle()


                # Pontuação final
                placar.clear()
                placar.goto(0, -40)

                placar.write(
                    f"Pontuação Final: {pontosf}",
                    align="center",
                    font=("Impact", 24, "normal")
                )


                # Fase final
                fases.clear()
                fases.goto(0, -70)
                fases.write(
                    f"Fase: {fase}",
                    align="center",
                    font=("Impact", 24, "normal")
                )


                # Mensagem para reiniciar
                texto_anuncio.clear()
                texto_anuncio.goto(0, -100)

                texto_anuncio.write(
                    "Pressione 'R' para Reiniciar",
                    align="center",
                    font=("Courier", 18, "bold")
                )

                janela.update()


janela.mainloop()