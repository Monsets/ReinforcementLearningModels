import numpy as np
import copy

from obstacle import Obstacle

class World():
    def __init__(self, canvas, obj, window_size):
        self.canvas = canvas
        self.obstacles = [Obstacle('rectangle', 50, 50, 100, 100),
                          Obstacle('rectangle', 150, 150, 200, 200),
                          Obstacle('rectangle', 50, 150, 100, 200),
                          Obstacle('rectangle', 150, 50, 200, 100)]
        self.target = [175, 175, 175, 175]
        self.obj = obj
        self.init_obj = obj.save_obj()
        self.window_width = window_size[0]
        self.window_height = window_size[1]
        self.time = 1.

    def draw(self):
        for obst in self.obstacles:
            if obst.type == 'rectangle':
                self.canvas.create_rectangle(obst.x1, obst.y1, obst.x2, obst.y2)
            if obst.type == 'oval':
                self.canvas.create_oval(obst.x1, obst.y1, obst.x2, obst.y2)

    def _collision(self):
        for obst in self.obstacles:
            if self.obj.x > obst.x1 and self.obj.x < obst.x2 and \
                self.obj.y > obst.y1 and self.obj.y < obst.y2:
                    return True
        if self.obj.x > self.window_width or self.obj.x < 0 or \
                self.obj.y > self.window_height or self.obj.y < 0:
            return True

        return False

    def _get_reward(self):
        return self.time * 1 / np.sqrt((self.obj.x - self.target[0])**2 + (self.obj.y - self.target[0]) ** 2)

    def _get_state(self):
        state = [self.obj.x, self.obj.y, self.obj.velocity, self.obj.angle]
        return state

    def get_init_state(self):
        state = self._get_state()
        return state

    def reset(self):
        self.obj.load_obj(self.init_obj)
        print(self.obj.save_obj())
        self.time = 1.
        return self._get_state()

    def make_action(self, action):
        if action < 2:
            self.obj.turn(action)
        else:
            self.obj.change_velocity(action % 2)
        self.obj.move()
        self.time -= 1e-4
        collision = self._collision()
        reward = self._get_reward()
        if collision:
            reward = 0
        state = self._get_state()

        return collision, reward, state
    