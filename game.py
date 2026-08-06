'''
* Aula 4
* Sistema de Pontuação: 
Criar um ator de texto na parte superior da tela para somar 1 ponto a cada colisão do laser com o inimigo.
'''

# Import
import turtle
import math #faz calculos
import random #sorteia numeros pseudoaleatórios

# Janela
janela = turtle.Screen()
janela.title("Gamezinho")
janela.bgpic("gif/espaco.gif")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)

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
inimigo.shape("circle")
inimigo.color("red")
inimigo.penup()
inimigo.goto(random.randint(-360, 360), 280) # o X é aleatório, de -360 a 360, o Y é 280
inimigo_vel = 0.05

#laser
laser = turtle.Turtle()
janela.addshape("gif/laser.gif")
laser.shape("gif/laser.gif")
laser.color("pink")
laser.shapesize(stretch_wid=1, stretch_len=0.2)
laser.penup()
laser.hideturtle() #esconde
laser_vel = 0.5
laser_estado = "pronto"

#placar
pontos = 0
placar = turtle.Turtle()
placar.speed(0)
placar.color("#7947c9")
placar.penup()
placar.hideturtle()
placar.goto(-315, 230)
placar.write(f"Pontos:{pontos}", align="center", font=("Impact", 20, "normal")) # escreve

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
            placar.clear()
            placar.write(f"Pontos: {pontos}", align="center", font=("Impact", 20, "normal"))
