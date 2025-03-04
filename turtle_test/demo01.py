import turtle
import random

# Fenster erstellen
window = turtle.Screen()
window.title("Zufällige Linien")
window.bgcolor("black")
window.setup(width=800, height=800)

# Turtle-Objekt erstellen
zeichner = turtle.Turtle()
zeichner.speed(0)  # Schnellste Geschwindigkeit
zeichner.pensize(2)
zeichner.pencolor("white")
zeichner.penup()
zeichner.goto(0, 0)
zeichner.pendown()

linien_anzahl = 0

def zufallsrichtung():
    winkel = random.randint(0, 360)
    zeichner.setheading(winkel)  # Setzt die Ausrichtung auf den Winkel
    länge = random.randint(50, 150)
    zeichner.forward(länge)

while True:
    zufallsrichtung()
    linien_anzahl += 1
    
    # Nach 50 Linien Bildschirm löschen
    if linien_anzahl >= 50:
        zeichner.clear()
        linien_anzahl = 0

window.mainloop()
