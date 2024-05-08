from turtle import Turtle as t
from player import Jugador
from pong import marcador, mover_pelota

paddleA = Jugador(-350, 0)
paddleB = Jugador(350, 0)
wn = t.screen()
marcador()
wn.listen()  # Escuchar los eventos de teclado
wn.onkeypress(paddleA.forward, "w")  # Avanzar hacia adelante con la tecla "w"
wn.onkeypress(paddleA.backward, "s")  # Retroceder hacia atrás con la tecla "s"
wn.mainloop()

