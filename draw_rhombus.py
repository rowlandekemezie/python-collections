from turtle import Turtle, Screen


def draw_rhombus(art, len):
    for i in range(4):
        art.forward(len)
        if (i == 0 or i == 2):
            art.right(60)
        else:
            art.right(120)
        art.forward(4.5)


def draw_art():
    window = Screen()
    window.bgcolor('cyan')
    angie = Turtle()
    angie.shape('turtle')
    angie.color('blue')
    angie.speed(2000)

  #  angie.left(105)
    for j in range(80):
        angie.right(5)
        draw_rhombus(angie, 100)

    angie.left(90)
    angie.forward(300)

    # Close window
    window.exitonclick()

draw_art()
