
import turtle as tl
from turtle import Turtle
tl = Turtle()
tl.speed(1000)
import turtle as tl


def draw_fractal(size):
    if size >= 5:	    
        draw_fractal(size / 3.0)	 
        tl.left(60)	        
        draw_fractal(size / 3.0)	 
        tl.right(120)	    
        draw_fractal(size / 3.0)	
        tl.left(60)	
        draw_fractal(size / 3.0)
    else:	   
        tl.forward(size)	


size = 200	
tl.pensize(2)
tl.penup()	
tl.goto(-size, -size/4)	
tl.pendown()	

for i in range(6):
    draw_fractal(size)
    tl.right(60)	
tl.done()	