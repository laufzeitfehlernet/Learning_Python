#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 10:18:16 2025

@author: snow
"""

import turtle

def zeichne_quad():
  for i in range(1,5):
      turtle.forward(75)
      turtle.left(90)
 

turtle.shape("turtle")
turtle.speed(0)
for i in range(0,24):
  zeichne_quad()
  turtle.left(15)

turtle.exitonclick()
