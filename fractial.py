
import turtle as tl
from turtle import Turtle
tl = Turtle()
tl.speed(1000)
def draw_fractal(scale):
    if scale >= 5:
        tl.forward(scale)
        tl.right(20)
        draw_fractal(scale / 1.5)
        tl.left(60)
        draw_fractal(scale / 1.5)
        tl.right(40)
        tl.right(20)
        draw_fractal(scale / 3.0)
        tl.left(20)
        tl.penup()
        tl.backward(scale)
        tl.pendown()
           
tl.left(90)        
scale = 200
tl.pencolor('green')
tl.pensize(2)
tl.penup()            
tl.goto(0, -scale)
tl.pendown()
draw_fractal(scale)
#tl.done()
    