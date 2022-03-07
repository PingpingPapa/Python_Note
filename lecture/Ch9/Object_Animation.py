from cs1graphics import *
import time

canvas = Canvas(1000, 600)
canvas.setBackgroundColor("light blue")
canvas.setTitle("cs101 Chick")

class Chicken(object):
    """Graphic representatin of a chicken"""
    def __init__(self, hen = False):
        self.layer = Layer()
        if hen:
            self.body = Ellipse(70, 80)
            self.body.setFillColor("white")
        else:
            self.body = Ellipse(40, 50)
            self.body.setFillColor("yellow")
            self.body.move(0, 10)

        self.body.setBorderColor("yellow")
        self.body.setDepth(20)
        self.layer.add(self.body)



    def move(self, dx, dy):
        self.layer.move(dx, dy)

print(1)
hen = Chicken(True)
chick1 = Chicken()
chick1.layer.move(120, 0)

print(12)
herd = Layer()
herd.add(hen.layer)
herd.add(chick1.layer)
herd.move(600, 200)

print(123)
chick2 = Chicken()
chick2.layer.move(500,200)

canvas.add(herd)
canvas.add(chick2.layer)