'''
Desafio 2: Sistema de Tiro :
Baixar desenhos , imagens na extensão .GIF e substituir o "Tiro"Verificar a necessidade de definir novo limite de tela dependendo do tamanho do objeto.
Anexar Link do Drive ou github com o material.
'''

# Import
import turtle

# Janela
janela = turtle.Screen()
janela.title("Gamezinho")
janela.bgpic("gif/espaco.gif")
janela.setup(width=800, height=600)

#nave
nave = turtle.Turtle()
janela.addshape("gif/nave.gif")
nave.shape("gif/nave.gif")

nave.color("#cb85f3")
nave.penup() #não deixa linha
nave.setheading(90) #apontando pra cima
nave.goto(0, -240) #posição

#laser
laser = turtle.Turtle()
janela.addshape("gif/laser.gif")
laser.shape("gif/laser.gif")
laser.color("pink")
laser.shapesize(stretch_wid=0.2, stretch_len=0.8)
laser.penup()
laser.setheading(90)
laser.hideturtle() #esconde
laser_vel = 20
laser_estado = "pronto"

#movimentos
def vaiEsquerda():
    x = nave.xcor()
    if x > -370: #limite borda esquerda
        nave.setx(x - 20)

def vaiDireita():
    x = nave.xcor()
    if x < 370: #limite borda direita
        nave.setx(x + 20)

def vaiCima():
    y = nave.ycor()
    if y < 240: #limite borda cima
        nave.sety(y + 20)

def vaiBaixo():
    y = nave.ycor()
    if y > -240: #limite borda baixo
        nave.sety(y - 20)

def vaiLaser():
    global laser_estado
    if laser_estado == "pronto":
        laser_estado = "disparado"
        x = nave.xcor()
        y = nave.ycor() + 10
        laser.goto(x, y)
        laser.showturtle() #mostra

def moveLaser():
    global laser_estado
    if laser_estado == "disparado":
        y = laser.ycor()
        laser.sety(y + laser_vel)
        if laser.ycor() > 280:
            laser.hideturtle()
            laser_estado = "pronto"
    janela.ontimer(moveLaser, 20) #chama a função a cada 20 milisegundos





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
moveLaser()


janela.mainloop()
