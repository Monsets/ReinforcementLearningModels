import math

class Point():
    def __init__(self, canvas, x = 0, y = 0, width = 0, color = 'red', velocity = 0):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.color = color
        self.velocity = 1
        self.angle = 0 * math.pi / 180

        self.__turning_const = 2.4
        self.__velocity_const = 0.01

    def save_obj(self):
        return [self.x, self.y, self.velocity, self.angle]

    def load_obj(self, obj):
        dif_x = self.x - obj[0]
        dif_y = self.y - obj[1]
        self.x = obj[0]
        self.y = obj[1]
        self.velocity = obj[2]
        self.angle = obj[3]
        self.canvas.move(self.p, -dif_x, -dif_y)
        self.canvas.update()


    def draw(self):
        self.p = self.canvas.create_oval(self.x, self.y, self.x, self.y, width = self.width, fill = self.color)

    def move(self):
        x = self.velocity * math.cos(self.angle)
        y = self.velocity * math.sin(self.angle)
        self.canvas.move(self.p, x, y)
        self.x += x
        self.y += y
        self.canvas.update()

    def turn(self, option):
        '''
        :param option: 0 stands for nothing, 1 for left and 2 for right
        :return:
        '''
        if option == 2:
            return
        if option == 0:
            self.angle -= self.__turning_const * math.pi / 180
        if option == 1:
            self.angle += self.__turning_const * math.pi / 180

        self.angle %= math.pi * 2

    def change_velocity(self, option):
        '''0 for nothing, 1 for stop, 2 for add'''
        if option == 2:
            return
        if option == 0:
            self.velocity -= self.__velocity_const
            if self.velocity < 0:
                self.velocity = 0
        if option == 1:
            self.velocity += self.__velocity_const
            if self.velocity > 1:
                self.velocity = 1