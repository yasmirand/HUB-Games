'''
Desafio 1: Substituição de Assets e Recalibragem de Borda: 
Baixar desenhos , imagens na extensão .GIF e substituir a tela de fundo bem como o ator ("nave")
Verificar a necessidade de definir novo limite de tela dependendo do tamanho do objeto.
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





janela.mainloop()
