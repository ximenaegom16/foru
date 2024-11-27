import math 
from turtle import *

def hearta(R):
  return 15*math.sin(R)**3\

def heartb(R):
     return 12*math.cos(R)-5*\
         math.cos(2*R)-2*\
         math.cos(3*R)-\
         math.cos(4*R)

speed(60)
bgcolor("black")


for i in range(6000):
  goto(hearta(i)*20,heartb(i)*20)
  for j in range(5):
      color("red")
      goto(0,0)


penup()
goto(0, -300) 
color("white")
write("You are the reason\nmy heart beats", align="center", font=("Arial", 18, "bold"))

hideturtle() 
done()