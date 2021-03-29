####jogo feito por @kmandzzz em python####

import turtle
import time
import random

delay = 0.1

#score (pontuação)
score = 0
high_score = 0

#configurando a tela do jogo
wn = turtle.Screen()
wn.title("Jogo da Cobrinha by @kmandzzz")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) #desliga a atualização em tela

#cabeca da cobra
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#comida da cobra
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("dark red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

#funções
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def mover():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#comando do teclado
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#loop principal do jogo
while True:
    wn.update()

    #colisão com a borda da tela
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #esconder o segmento
        for segment in segments:
            segment.goto(1000, 1000)
        
        #limpar a lista de segmento
        segments.clear()

        #resetar o score(pontuação)
        score = 0

        #resetar o delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    #colisão com a comida
    if head.distance(food) < 20:
        #mover a comida para um lugar aleatório
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        #adicionando a lista de segmento
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #diminuindo o delay
        delay -= 0.001

        #aumentando o score(pontuação)
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # movimentação do corpo da cobra
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #movimentaçao do segmento 0 do corpo da cobra
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    mover()    

    #colisão da cabeça com os segmentos(corpo da cobra)
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            #esconde os segmentos
            for segment in segments:
                segment.goto(1000, 1000)
        
            #limpa a lista de segmentos
            segments.clear()

            #reseta a pontuação score
            score = 0

            #reseta o delay delay
            delay = 0.1
        
            #atualiza a tela de pontos
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()