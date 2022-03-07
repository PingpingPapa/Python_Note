from cs1graphics import *
import time
import math

canvas = Canvas(1500, 500)
canvas.setBackgroundColor("blue")
canvas.setTitle("cs101 Drawing excersize")

sun = Circle(15)
canvas.add(sun)
sun.setFillColor("yellow")

r = 800
for i in range(120):
    x = r * 0.5 * math.sqrt(3) - r * math.sin(math.radians(60-i))
    y = -r * math.cos(math.radians(60 - i)) + 400 + 500
    sun.moveTo(x, y)

    time.sleep(0.05)

'''
sq.setBorderWidth(5)
sq.moveTo(200, 200)

r = Rectangle(150, 75)
canvas.add(r)
r.setFillColor("yellow")



car = Layer()

tire1 = Circle(10, Point(-20, -10))
tire1.setFillColor('black')
car.add(tire1)

tire2 =Circle(10, Point(20, -10))
tire2.setFillColor('black')
car.add(tire2)

body = Rectangle(70, 30, Point(0, -25))
body.setFillColor('blue')
body.setDepth(60)
car.add(body)

canvas.add(car)
car.move(20,200)

for i in range(50):
    car.move(2,0)
    time.sleep(0.05)

for i in range(22):
    car.rotate(-1)
    time.sleep(0.05)

for i in range(50):
    car.move(2,-1)
    time.sleep(0.05)

for i in range(22):
    car.rotate(1)
    time.sleep(0.05)

for i in range(10):
    car.scale(1.05)
    time.sleep(0.05)
    '''
