#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 09:25:37 2025

@author: snow
"""

import turtle

def create_screen(title):
    screen = turtle.Screen()
    screen.title(title)
    return screen

def create_turtle(form, speed):
    t = turtle.Turtle()
    if form == 'none':
        t.hideturtle() # Versteckt die Turtle-Form
    else:
        t.shape(form)
    t.speed(0)
    return t

def draw_circle(t, x, y, radius):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(radius)
  
    
if __name__ == "__main__":
    screen = create_screen("Zeichne einen Kreis")
    my_turtle = create_turtle("none",0)
    
    x = 200
    y = 200
    
    draw_circle(my_turtle, x, y, 100)
    
    screen.exitonclick()
  
