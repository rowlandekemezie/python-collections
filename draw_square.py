 from webbrowser import open
from time import sleep
import turtle
import os

# opening of web browser using python
def browser():
    for i in range(3):
        sleep(10)
        open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
def me():
    print("Great day")

def great():
    print("How is the day going with you")

def rename(filenames):
    for file in filenames:
        os.rename(file, file.translate(None, '0123456789'))

# drawing a square using python
def draw_square(square):
    for i in range(4):
        square.forward(100)
        square.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('green')
    square = turtle.Turtle()
    square.shape('turtle')
    square.color('red')
    square.speed(2)

    for i in range(36):
        draw_square(square)
        square.right(10)

    window.exitonclick()
    
    
