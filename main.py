import time
import numpy as np

from tkinter import *
from point import Point
from world import World
from model import Model

def init_world():
    root = Tk()

    width = 600
    height = 600

    c = Canvas(root, width=width, height=height, bg='white')
    c.pack()

    p = Point(c, x=10, y=10, width=10)
    w = World(c, p, (width, height))

    p.draw()
    w.draw()

    return w

world = init_world()
m = Model(4, 4)

state = world.get_init_state()

while True:
    action = m.pred(state)
    if np.random.randint(0, 10) == 10:
        action = np.random.randint(0, 5)
    collision, reward, new_state = world.make_action(action)
    print(action)
    #print(collision)
    if collision:
        m.train(state, reward)
        state = world.reset()
        continue
    m.train(state, reward)
    state = new_state

    #time.sleep(0.02)

