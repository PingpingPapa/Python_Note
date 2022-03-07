from cs1graphics import *
import time

canvas = Canvas(400, 300)
canvas.setBackgroundColor("light blue")
canvas.setTitle("cs101 Drawing excersize")

sq = Square(100)
canvas.add(sq)
sq.setFillColor("blue")
sq.setBorderColor("red")
sq.setBorderWidth(5)
sq.moveTo(200, 200)
sq.rotate(45)
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
