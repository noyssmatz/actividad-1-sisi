"""Paint, for drawing shapes.

Exercises

1. Add a color.DONE
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""
from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(4):
        forward(end.x - start.x)
        left(90)
    end_fill()

def rectangle(start, end):
    "Draw complete rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    goto(end.x, start.y)
    goto(end.x, end.y)
    goto(start.x, end.y)
    goto(start.x, start.y)
    end_fill()

def tap(x, y):
    "Store start or draw shape."
    start = state['start']
    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
onscreenclick(tap)

listen()
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', rectangle), 'r')

onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')

done()
