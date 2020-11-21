
import turtle as tl
from turtle import Turtle
tl = Turtle()
tl.speed(1000)
def draw_fractal(scale):
    if scale >= 5:
        tl.forward(scale)
        tl.right(60)
        draw_fractal(scale/2)
        tl.left(60)
        draw_fractal(scale/1.5)
        tl.left(60)
        draw_fractal(scale/2)
        tl.right(60)
        tl.backward(scale)
scale = 100
tl.left(90)
tl.pencolor('green')
tl.pensize(2)
for i in range(6):
    draw_fractal(scale)
    tl.right(60)
tl.done()
    