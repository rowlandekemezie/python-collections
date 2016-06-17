from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.color = 'green'


# bob.delay = 0.01


def square(t, length):
    for i in xrange(4):
        fd(t, length)
        lt(t, 45)


def polygon(t, length, n):
    for i in xrange(n):
        bk(t, length)
        lt(t, 60)


def circle(t, r):
    polygon(t, r, 8)


# square(bob, 100)
# polygon(bob, 100, 6)
circle(bob, 100)
wait_for_user()
