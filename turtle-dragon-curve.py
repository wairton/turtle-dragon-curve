from sys import argv
from turtle import Turtle


def draw_dragon_curve(curve_data):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.forward(6)
    screen = turtle.getscreen()
    tracer_step = len(curve_data) / 40
    screen.tracer(tracer_step if tracer_step > 4 else 5,10)
    for datum in curve_data:
        if datum == 1:
            turtle.left(90)
        else:
            turtle.right(90)
        turtle.forward(5)
    return turtle


def generate_dragon_curve(iterations):
    state = [1]
    for i in xrange(iterations - 1):
        invert_index = -(len(state) + 1) / 2
        state = state + [1] + state
        state[invert_index] = 0
    return state


if __name__ == "__main__":
    turtle = draw_dragon_curve(generate_dragon_curve(int(argv[1])))
    turtle.getscreen().getcanvas().postscript(file="dragon.eps")
    raw_input("press a key to continue...")
