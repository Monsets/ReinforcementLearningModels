import time
import numpy as np

from tkinter import *
from point import Point
from world import World
from model import Model

def init_world():
    root = Tk()

    c = Canvas(root, width=600, height=600, bg='white')
    c.pack()

    p = Point(c, x=10, y=10, width=10)
    w = World(c, p)

    p.draw()
    w.draw()

    return w

world = init_world()
m = Model(2, 6)

state = world.get_init_state()

while True:
    preds = m.pred(state)
    action = [np.argmax(preds[:3]), np.argmax[3:]]
    collision, reward, state = world.make_action(action)
    if collision:
        state = world.reset()
        continue
    m.train(reward)

    time.sleep(0.02)

