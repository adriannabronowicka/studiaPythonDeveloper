"""
Zaimplementuj klasę turtle
atrybuty: x, y, direction
forward
backward
left
right
self.x = 0
self.y = 0
self.direction = "up"
"""

from typing import Literal

import matplotlib.pyplot as plt

class Turtle:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    # direction == 0 -> up
    # direction == 1 -> down
    # direction == 2 -> left
    # direction == 3 -> right

    def forward(self, amount):
        if self.direction == 0:
            self.y += amount
        elif self.direction == 1:
            self.y -= amount
        elif self.direction == 2:
            self.x -= amount
        elif self.direction == 3:
            self.x += amount
        return self.x, self.y

    def right(self,):
        if self.direction == 0:
            self.direction = 3
        elif self.direction == 1:
            self.direction = 2
        elif self.direction == 2:
            self.direction = 0
        elif self.direction == 3:
            self.direction = 1
        return self.direction

    def backward(self, amount):
        if self.direction == 0:
            self.y -= amount
        elif self.direction == 1:
            self.y += amount
        elif self.direction == 2:
            self.x += amount
        elif self.direction == 3:
            self.x -= amount
        return self.x, self.y

    def left(self):
        if self.direction == 0:
            self.direction = 2
        elif self.direction == 1:
            self.direction = 3
        elif self.direction == 2:
            self.direction = 1
        elif self.direction == 3:
            self.direction = 0
        return self.direction


zolwik = Turtle(0,0,0)

def my_custom_animal_path(turtle):
    points = [(0,0)]
    points.append(zolwik.forward(3))
    zolwik.right()
    points.append(zolwik.forward(2))
    zolwik.right()
    points.append(zolwik.backward(1))

    plt.scatter(*zip(*points))
    plt.plot(*zip(*points))
    plt.show()


my_custom_animal_path(zolwik)
