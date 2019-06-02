import numpy as np

from obstacle import Obstacle

class World():
    def __init__(self, canvas, obj):
        self.canvas = canvas
        self.obstacles = [Obstacle('rectangle', 50, 50, 100, 100),
                          Obstacle('rectangle', 150, 150, 200, 200),
                          Obstacle('rectangle', 50, 150, 100, 200),
                          Obstacle('rectangle', 150, 50, 200, 100)]
        self.target = [175, 175, 175, 175]
        self.obj = obj
        self.init_obj = obj

    def draw(self):
        for obst in self.obstacles:
            print(obst)
            if obst.type == 'rectangle':
                self.canvas.create_rectangle(obst.x1, obst.y1, obst.x2, obst.y2)
            if obst.type == 'oval':
                self.canvas.create_oval(obst.x1, obst.y1, obst.x2, obst.y2)

    def _collision(self):
        for obst in self.obstacles:
            if self.obj.x > obst.x1 and self.obj.x < obst.x2 and \
                self.obj.y > obst.y1 and self.obj.y < obst.y2:
                    return True

        return False

    def _get_reward(self):
        return np.sqrt((self.obj.x - self.target[0])**2 + (self.obj.y - self.target[0]) ** 2)

    def _get_state(self):
        state = [self.obj.velicity, self.obj.angle]
        return state

    def get_init_state(self):
        state = self._get_state()
        return state

    def reset(self):
        self.obj = self.init_obj
        return self._get_state()

    def make_action(self, action):

        self.obj.turn(action[0])
        self.obj.change_velocity(action[1])
        self.obj.move()

        collision = self._collision()
        reward = self._get_reward()
        state = self._get_state()

        return collision, reward, state
    