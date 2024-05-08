import turtle
from pong import *

class Jugador:
    def __init__(self, x, y):
        self.y = y
        self.x = x
        
        # Inicializar la tortuga para el jugador
        self = turtle.Turtle()
        self.shape("square")
        self.shapesize(5, 1)
        self.speed(0)
        self.color("white")
        self.penup()  # Levantar el lápiz para que no dibuje al moverse
        self.goto(x ,y)  # Posicionar la tortuga en las coordenadas iniciales

    def forward(self):
        # Mover hacia adelante
        y = self.ycor()
        y += 40
        self.sety(y)

    def backward(self):
        # Mover hacia atrás
        y = self.ycor()
        y -= 40
        self.sety(y)